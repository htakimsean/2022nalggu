from django import forms

from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user', 'tel', 'email', 'address', 'postal_code']