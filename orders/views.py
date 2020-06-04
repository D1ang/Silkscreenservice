from django.shortcuts import render
from .models import Item


def item_list(request):
    """
    A view that displays all the products
    on the services page.
    """
    context = {'items': Item.objects.all()}

    return render(request, 'orders/item_list.html', context)
