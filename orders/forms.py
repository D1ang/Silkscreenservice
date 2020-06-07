from django import forms
from django_countries.fields import CountryField


PAYMENT_CHOICES = (
    ('stripe', 'Stripe'),
    ('paypal', 'Paypal')
)


class CheckoutForm(forms.Form):
    address = forms.CharField()
    address_number = forms.CharField()
    country = CountryField(blank_label='(select country)')
    postal = forms.CharField()
    same_billing_address = forms.BooleanField(widget=forms.CheckboxInput())
    save_info = forms.BooleanField(widget=forms.CheckboxInput())
    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAYMENT_CHOICES)
