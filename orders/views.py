from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, ListView, DetailView
from .models import Item, OrderItem, Order


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
            return redirect('orders:service', slug=slug)
    else:
        order = Order.objects.create(user=request.user)
        order.items.add(order_item)
        messages.info(request, 'Selected service was added to the cart.')
        return redirect('orders:service', slug=slug)


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
            return redirect('orders:service', slug=slug)
        else:
            messages.info(request, 'This service was not in your cart.')
            return redirect('orders:service', slug=slug)
    else:
        messages.info(request, 'You do not have an active order.')
        return redirect('orders:service', slug=slug)
