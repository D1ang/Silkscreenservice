from .decorators import allowed_users
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from orders.models import Order
from orders.forms import OrderForm

from .models import Customer
from .forms import CustomerForm
from .filters import OrderFilter


@login_required
@allowed_users(allowed_roles=['admin'])
def adminpage(request):
    """
    A view that displays the dashboard
    for the admin & paginate the order list.
    """
    customer_list = Customer.objects.all()
    total_customers = customer_list.count()

    order_list = Order.objects.all().order_by('-date')
    total_orders = order_list.count()
    pending_orders = order_list.filter(status='pending').count()
    finished_orders = order_list.filter(status='finished').count()

    orderFilter = OrderFilter(request.GET, queryset=order_list)
    order_list = orderFilter.qs

    paginator = Paginator(order_list, 6)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    context = {
        'customer_list': customer_list,
        'total_customers': total_customers,
        'page_object': page_object,
        'total_orders': total_orders,
        'pending_orders': pending_orders,
        'finished_orders': finished_orders,
        'orderFilter': orderFilter,
    }
    return render(request, 'accounts/adminpage.html', context)


@login_required
@allowed_users(allowed_roles=['customer'])
def customerpage(request):
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
    return render(request, 'accounts/customerpage.html', context)


@login_required
def orderdetails(request, pk_order):
    """
    A orderdetail page for the customer to view the selected
    order and be able to download the provided artwork.
    """
    order = Order.objects.get(id=pk_order)
    tax = order.get_total() / 100 * 21
    total = order.get_total() + tax

    context = {
        'order': order,
        'tax': tax,
        'total': total
    }
    return render(request, 'accounts/orderdetails.html', context)


@login_required
@allowed_users(allowed_roles=['admin'])
def update_order(request, pk_order):
    """
    A order update page for the admin to change the status
    and download/upload the artwork for the customer.
    """
    order = Order.objects.get(id=pk_order)
    form = OrderForm(instance=order)
    tax = order.get_total() / 100 * 21
    total = order.get_total() + tax

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.info(request, 'Order updated successfully')
            return redirect('accounts:adminpage')
    else:
        context = {
            'order': order,
            'tax': tax,
            'total': total,
            'form': form
        }
        return render(request, 'accounts/update_order.html', context)


@login_required
def userprofile(request):
    """
    Profile settings for the user,
    to change/update their own profile.
    """
    customer = request.user.customer
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            messages.info(request, 'Profile update successfully')
            return redirect('accounts:customerpage')
    else:
        context = {'form': form}
        return render(request, 'accounts/userprofile.html', context)
