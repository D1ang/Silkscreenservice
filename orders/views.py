from django.shortcuts import render
from .models import Item


def item_list(request):
    """
    A view that lists all the
    available items/services
    """
    context = {'items': Item.objects.all()}

    return render(request, 'orders/item_list.html', context)
