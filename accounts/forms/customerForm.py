from django.forms import ModelForm, fields
from ..models import Customer


class customerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']