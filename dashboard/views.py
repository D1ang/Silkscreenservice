from django.shortcuts import render


def dashboard(request):
    """
    A view that displays the dashboard
    for the customers.
    """

    return render(request, 'dashboard.html')
