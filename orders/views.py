from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, ListView
from .models import Item, OrderItem, Order
from decimal import Decimal


class ItemListView(ListView):
    """
    Shows all the available services/products
    on 1 page.
    """
    model = Item
    template_name = 'orders/services.html'


class OrderSummaryView(LoginRequiredMixin, View):
    """
    A cart that shows the ordered services and
    precalculates the totals, inclusing tax.
    When cart is zero or no active order a warning
    message will be shown to the user.
    """
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            tax = order.get_total() * Decimal(21 / 100)
            total = order.get_total() + tax

            if total < 1:
                messages.warning(self.request, 'Your cart is empty')
                return redirect('/services')
            else:
                context = {
                    'object': order,
                    'tax': tax,
                    'total': total
                }
                return render(self.request, 'orders/cart.html', context)

        except ObjectDoesNotExist:
            messages.warning(self.request, 'There is no active order')
            return redirect('orders:services')


@login_required
def add_to_cart(request, slug):
    """
    Adds an item to the cart, creates an order and
    checks if an item already is in the order.
    Adds 1 popularity click.
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
            messages.error(
                request, 'Only one of the same allowed')
            return redirect('orders:services')
        else:
            order.items.add(order_item)

            item.clicks += 1
            item.save()

            messages.info(request, 'Service is added to the cart')
            return redirect('orders:cart')
    else:
        order = Order.objects.create(user=request.user)
        order.items.add(order_item)
        messages.info(request, 'Service is added to the cart')
        return redirect('orders:cart')


@login_required
def remove_from_cart(request, slug):
    """
    Checks if the item is in the cart
    and removes it if there is an active order.
    Removes 1 popularity click.
    """
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]

        # check if the item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)

            item.clicks -= 1
            item.save()

            messages.info(request, 'Service removed from cart')
            return redirect('orders:cart')
        else:
            messages.info(request, 'Service not in your cart')
            return redirect('orders:cart')
    else:
        messages.info(request, 'There is\'nt an active order')
        return redirect('orders:cart')
