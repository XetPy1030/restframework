from django import forms

from .models import Product, Cart, CartItem

class ProductForm(forms.ModelForm):
    class Meta:
            model = Product
            fields = '__all__'


class CartItemForm(forms.ModelForm):
    class Meta:
            model = CartItem
            fields = '__all__'


class CartForm(forms.ModelForm):
    class Meta:
            model = Cart
            fields = '__all__'