# Generated by Django 4.0.1 on 2022-02-09 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_customer_order_shippingaddress_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
