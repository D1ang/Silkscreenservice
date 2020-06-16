from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from orders.models import Order
from .forms import CustomerForm


@login_required
def dashboard(request):
    """
    A view that displays the dashboard
    for the customer & paginate the order list.
    """
    order_list = request.user.order_set.all().order_by('-date')
    paginator = Paginator(order_list, 6)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    total_orders = order_list.count()
    pending_orders = order_list.filter(status='pending').count()
    finished_orders = order_list.filter(status='finished').count()

    context = {
        'page_object': page_object,
        'total_orders': total_orders,
        'pending_orders': pending_orders,
        'finished_orders': finished_orders,
    }

    return render(request, 'dashboard/customer.html', context)


@login_required
def orderdetails(request, pk_order):
    """
    Updating an exciting order.
    """
    order = Order.objects.get(id=pk_order)

    context = {
        'order': order,
    }

    return render(request, 'dashboard/orderdetails.html', context)


@login_required
def userprofile(request):
    """
    Authenticated profile settings for the user
    to change the profile settings.
    """
    customer = request.user.customer
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            messages.info(request, 'Profile update successfully')
            return redirect('dashboard:dashboard')
    else:
        context = {'form': form}
        return render(request, 'dashboard/userprofile.html', context)
