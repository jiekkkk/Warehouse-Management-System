from django.db import models
from django.contrib.auth.models import User

# Create your models here.
status_category = ( # for the choice in below class
    ('ship', 'Ship'),
    ('restock', 'Restock'),
)

class Product(models.Model):
    po_number = models.PositiveIntegerField(null=True)
    date_of_receiving_po = models.DateField(null=True, blank=True)
    company = models.CharField(max_length=1000, null=True)
    estimated_date_arrival = models.DateField(null=True, blank=True)
    item = models.CharField(max_length=1000, null=True)
    qty = models.PositiveIntegerField(null=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    do_number = models.PositiveIntegerField(null=True, blank=True) # when DO reached
    description = models.CharField(max_length=1000, null=True, blank=True) # record the condition when DO reached

    class Meta:
        verbose_name_plural = 'Product' # rename in localhost

    def __str__(self): # to display the name in the list
        return f'{self.item}'


class Order(models.Model):
    po_number = models.PositiveIntegerField(null=True)
    date_generate = models.DateTimeField(auto_now_add=True)
    client = models.CharField(max_length=255, null=True)
    item = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    qty = models.PositiveIntegerField(null=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True)

    class Meta:
        verbose_name_plural = 'Order' # rename in localhost

    def __str__(self):
        return f'{self.item}_{self.qty}'
    