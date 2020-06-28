from django import forms
from django.forms import ModelForm
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget  # noqa: F401
from orders.models import Order


class OrderForm(ModelForm):
    """
    A orderform for editting an order by
    the admin trough the admin's dashboard.
    """
    class Meta:
        model = Order
        fields = ['status', 'artwork']


class CheckoutForm(forms.Form):
    """
    A checkout form that collects the customer
    Billing address and prefered payment option.
    """
    first_name = forms.CharField()
    last_name = forms.CharField()
    street_address = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': '1234 Main street'}))
    address_line_2 = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Appartment or floor'}))
    city = forms.CharField()
    region = forms.CharField()
    postal = forms.CharField()
    country = CountryField(blank_label='Select country').formfield()
    artwork = forms.FileField()
