# Generated by Django 5.0.7 on 2024-07-26 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_product_po_number_product_company_product_item_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='company',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
