from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import CheckoutForm
from .models import Order, BillingAddress, Payment
from accounts.models import Customer
from decimal import Decimal
import stripe
import random
import string


stripe_public_key = settings.STRIPE_PUBLIC_KEY
stripe_secret_key = settings.STRIPE_SECRET_KEY


def create_id_code():
    return ''.join(
        random.choices(string.ascii_uppercase + string.digits, k=8)
    )


class CheckoutView(LoginRequiredMixin, View):
    """
    Sends the checkout form if its valid with
    the customer address info and prefered
    payment option.
    """
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            customer = Customer.objects.get(user=self.request.user)
            total = order.get_total()

            if total < 1:
                messages.warning(self.request, 'Your cart is empty')
                return redirect('orders:services')
            else:
                form = CheckoutForm(initial={
                  'company_name': customer.company_name,
                  'first_name': customer.first_name,
                  'last_name': customer.last_name,
                  'street_address': customer.street_address,
                  'address_line_2': customer.address_line_2,
                  'city': customer.city,
                  'region': customer.region,
                  'postal': customer.postal,
                  'country': customer.country
                })
                context = {'form': form}
                return render(self.request, 'orders/checkout.html', context)
        except ObjectDoesNotExist:
            messages.warning(self.request, 'There is no active order')
            return redirect('orders:services')

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST, self.request.FILES or None)
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            if form.is_valid():
                company_name = form.cleaned_data.get('company_name')
                first_name = form.cleaned_data.get('first_name')
                last_name = form.cleaned_data.get('last_name')
                street_address = form.cleaned_data.get('street_address')
                address_line_2 = form.cleaned_data.get('address_line_2')
                city = form.cleaned_data.get('city')
                region = form.cleaned_data.get('region')
                postal = form.cleaned_data.get('postal')
                country = form.cleaned_data.get('country')
                artwork = form.cleaned_data.get('artwork')
                comments = form.cleaned_data.get('comments')
                billing_address = BillingAddress(
                    user=self.request.user,
                    company_name=company_name,
                    first_name=first_name,
                    last_name=last_name,
                    street_address=street_address,
                    address_line_2=address_line_2,
                    city=city,
                    region=region,
                    postal=postal,
                    country=country
                )
                billing_address.save()
                order.billing_address = billing_address
                order.artwork = artwork
                order.comments = comments
                order.save()

                return redirect('orders:payment')

        except ObjectDoesNotExist:
            messages.warning(self.request, 'There is no active order')
            return redirect('orders:checkout')


class PaymentView(LoginRequiredMixin, View):
    """
    Load the payment view and loads the public
    Stripe key for the card field.
    """
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            tax = order.get_total() * Decimal(21 / 100)
            total = order.get_total() + tax

            if total < 1:
                messages.warning(self.request, 'Your cart is empty')
                return redirect('orders:services')

            if order.billing_address:
                stripe.api_key = stripe_secret_key

                template = 'orders/payment.html'
                context = {
                    'order': order,
                    'stripe_public_key': stripe_public_key,
                    'client_secret': stripe_secret_key,
                    'tax': tax,
                    'total': total
                }
                return render(self.request, template, context)
            else:
                messages.warning(
                    self.request, 'Billing address is missing')
                return redirect('orders:checkout')
        except ObjectDoesNotExist:
            messages.warning(self.request, 'There is no active order')
            return redirect('orders:services')

    def post(self, *args, **kwargs):
        """
        When POST payment will be created in the database
        and on Stripe.
        """
        stripe.api_key = stripe_secret_key

        order = Order.objects.get(user=self.request.user, ordered=False)
        tax = order.get_total() * Decimal(21 / 100)
        total = order.get_total() + tax

        token = self.request.POST.get('stripeToken')
        amount = int(total * 100)
        charge = stripe.Charge.create(
            amount=amount,
            currency='eur',
            description='Silkscreenservice order',
            source=token
        )

        # Creating the payment
        payment = Payment()
        payment.stripe_charge_id = charge['id']
        payment.user = self.request.user
        payment.amount = amount
        payment.save()

        # Assign payment to order
        order_items = order.items.all()
        order_items.update(ordered=True)
        for item in order_items:
            item.save()

        order.ordered = True
        order.payment = payment
        order.total = total
        order.tax = tax
        order.id_code = '920-' + create_id_code()
        order.save()

        messages.success(self.request, 'Your order was successful!')
        return redirect('accounts:customerpage')
