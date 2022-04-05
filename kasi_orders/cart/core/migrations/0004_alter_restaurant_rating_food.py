# Generated by Django 4.0.1 on 2022-01-13 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_restaurants_restaurant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='rating',
            field=models.FloatField(max_length=2),
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('Meal', 'Meal'), ('Platter', 'Platter'), ('Drink', 'Drink')], max_length=100)),
                ('price', models.FloatField(max_length=6)),
                ('rating', models.FloatField(max_length=2)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.restaurant')),
            ],
        ),
    ]