from django.contrib import admin
from .models import Product, Order
from django.contrib.auth.models import Group 

admin.site.site_header = 'Maxim WMS'

class ProductAdmin(admin.ModelAdmin): # to show in localhost
    list_display = ['po_number', 'item', 'estimated_date_arrival', 'do_number', 'qty']
    list_filter = ['estimated_date_arrival', 'item', 'do_number']

class OrdersAdmin(admin.ModelAdmin): # to show in localhost
    list_display = ['po_number', 'item', 'qty']

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrdersAdmin)

# admin.site.unregister(Group) # incase we dun need it
