from django.db import models
from django.contrib.auth.models import User


class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    tags = models.TextField()
    distance = models.CharField(max_length=10)
    rating = models.FloatField(max_length=2)

    def __str__(self) -> str:
        return self.name


class Food(models.Model):
    Category = [
        ('Meal', 'Meal'),
        ('Platter', 'Platter'),
        ('Drink', 'Drink')
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=Category)
    price = models.FloatField(max_length=6)
    rating = models.FloatField(max_length=2)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL,null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    product = models.ForeignKey(Food, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=4, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
