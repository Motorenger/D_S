from django import forms

from .models import Cart


class CartForm(forms.ModelForm):

    class Meta:
        model = Cart
        fields = ('user', 'sum', 'products')
