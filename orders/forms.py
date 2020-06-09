from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget  # noqa: F401


PAYMENT_CHOICES = (
    ('stripe', 'Stripe'),
    ('paypal', 'Paypal')
)


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
    save_info = forms.BooleanField(
        required=False, widget=forms.CheckboxInput())
    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAYMENT_CHOICES)
