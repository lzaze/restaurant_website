# Generated by Django 4.0.1 on 2022-01-12 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_restaurant_name_restaurants_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Restaurants',
            new_name='Restaurant',
        ),
    ]