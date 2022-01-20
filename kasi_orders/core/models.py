from django.db import models


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
