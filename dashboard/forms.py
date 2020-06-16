from django.forms import ModelForm
from .models import Customer


class CustomerForm(ModelForm):
    """
    A customer edit profile form.
    'user' is excluded to probhit username edditing.
    """
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']
