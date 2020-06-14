from django.shortcuts import render
from orders.models import Item


def index(request):
    """
    A view that displays the index page and renders
    the three most clicked services.
    """
    items = Item.objects.all().order_by('-clicks')[:3]

    context = {'items': items}

    return render(request, 'home/index.html', context)
