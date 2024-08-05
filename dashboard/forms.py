from django import forms
from .models import Product, Order


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class OrdersForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['po_number', 'client', 'item', 'qty', 'unit_price', 'total']