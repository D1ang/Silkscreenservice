from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, ListView, DetailView
from .forms import CheckoutForm
from .models import Item, OrderItem, Order, BillingAddress, Payment
import stripe


stripe_public_key = settings.STRIPE_PUBLIC_KEY
stripe_secret_key = settings.STRIPE_SECRET_KEY


class ItemListView(ListView):
    model = Item
    template_name = 'services_list.html'


class ItemDetailView(DetailView):
    model = Item
    template_name = 'service_details.html'


class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):

        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {'object': order}
            return render(self.request, 'cart.html', context)
        except ObjectDoesNotExist:
            messages.error(self.request, 'You do not have an active order')
            return redirect('/')


class CheckoutView(View):
    """
    Sends the checkout form if its valid with
    the customer address info and prefered
    payment option.
    """

    def get(self, *args, **kwargs):
        form = CheckoutForm()
        context = {'form': form}
        return render(self.request, 'checkout.html', context)

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            if form.is_valid():
                first_name = form.cleaned_data.get('first_name')
                last_name = form.cleaned_data.get('last_name')
                street_address = form.cleaned_data.get('street_address')
                address_line_2 = form.cleaned_data.get('address_line_2')
                city = form.cleaned_data.get('city')
                region = form.cleaned_data.get('region')
                postal = form.cleaned_data.get('postal')
                country = form.cleaned_data.get('country')
                # TODO: add functionality to these fields.
                # save_info = form.cleaned_data.get('save_info')
                payment_option = form.cleaned_data.get('payment_option')
                billing_address = BillingAddress(
                    user=self.request.user,
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
                order.save()

                if payment_option == 'stripe':
                    return redirect('orders:payment', payment_option='stripe')
                elif payment_option == 'paypal':
                    return redirect('orders:payment', payment_option='paypal')
                else:
                    messages.warning(self.request, 'Invalid payment option')
                    return redirect('orders:checkout')

        except ObjectDoesNotExist:
            messages.error(self.request, 'You do not have an active order')
            return redirect('orders:checkout')


class PaymentView(View):
    """
    Load the payment view and loads the public
    Stripe key for the card field.
    """
    def get(self, *args, **kwargs):
        order = Order.objects.get(user=self.request.user, ordered=False)
        stripe.api_key = stripe_secret_key

        template = 'payment.html'
        context = {
            'order': order,
            'stripe_public_key': stripe_public_key,
            'client_secret': stripe_secret_key,
        }
        return render(self.request, template, context)

    def post(self, *args, **kwargs):
        """
        When POST payment will be created in the database
        and on Stripe.
        """
        stripe.api_key = stripe_secret_key

        order = Order.objects.get(user=self.request.user, ordered=False)
        token = self.request.POST.get('stripeToken')
        amount = int(order.get_total() * 100)
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
        order.ordered = True
        order.payment = payment
        order.save()

        messages.success(self.request, 'Your order was successful!')
        return redirect('/')


@login_required
def add_to_cart(request, slug):
    """
    Adds an item to cart and creates an order
    checks if an item already is in the order.
    """
    item = get_object_or_404(Item, slug=slug)

    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False,
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]

        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            messages.info(
                request, 'Only one of the same service in the cart allowed')
            return redirect('orders:service', slug=slug)
        else:
            order.items.add(order_item)

            item.clicks += 1
            item.save()

            messages.info(request, 'Selected service was added to the cart.')
            return redirect('orders:cart')
    else:
        order = Order.objects.create(user=request.user)
        order.items.add(order_item)
        messages.info(request, 'Selected service was added to the cart.')
        return redirect('orders:cart')


@login_required
def remove_from_cart(request, slug):
    """
    Removes an item from cart.
    """
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]

        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)

            item.clicks -= 1
            item.save()

            messages.info(request, 'Selected service was removed from cart.')
            return redirect('orders:cart')
        else:
            messages.info(request, 'This service was not in your cart.')
            return redirect('orders:service', slug=slug)
    else:
        messages.info(request, 'You do not have an active order.')
        return redirect('orders:service', slug=slug)
