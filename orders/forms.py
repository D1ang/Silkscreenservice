from django import forms
from crispy_forms.helper import FormHelper
from orders.models import Order


class OrderForm(forms.ModelForm):
    """
    A orderform for editting an order by
    the admin trough the admin's dashboard.
    """
    helper = FormHelper()
    helper.form_show_labels = True

    class Meta:
        model = Order
        fields = ('status', 'artwork', 'comments')

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['comments'].widget.attrs.update(
            {
                'class': 'new-res-description',
                'placeholder': 'max 250 characters',
                'rows': 7
            })
