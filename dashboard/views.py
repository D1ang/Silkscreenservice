from django.shortcuts import render
from orders.models import Order


def dashboard(request):
    """
    A view that displays the dashboard
    for the customers.
    """
    customer = request.user
    orders = request.user.order_set.all()

    total_orders = orders.count()

    total_orders = orders.count()
    pending_orders = orders.filter(status='pending').count()
    finished_orders = orders.filter(status='finished').count()

    context = {
        'customer': customer,
        'orders': orders,
        'total_orders': total_orders,
        'pending_orders': pending_orders,
        'finished_orders': finished_orders,
    }

    print(context)

    return render(request, 'dashboard.html', context)
