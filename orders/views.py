from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Item, OrderItem, Order


class ItemListView(ListView):
    model = Item
    template_name = 'product_list.html'


class ItemDetailView(DetailView):
    model = Item
    template_name = 'product.html'


def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            # QUANTITY IS NOT NEEDED!!!!
            print('Item already in database!')
            order_item.quantity += 1
            order_item.save()
        else:
            order.items.add(order_item)
    else:
        order = Order.objects.create(user=request.user)
        order.items.add(order_item)
    return redirect('orders:product', slug=slug)
