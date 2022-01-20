from django.views.generic import View
from django.shortcuts import render
from .models import Food, Restaurant


class HomeView(View):

    @staticmethod
    def get(request):
        context = {
            'res': Restaurant.objects.all()
        }
        return render(request, "home.html", context)


class RestaurantView(View):

    @staticmethod
    def get(request, pk):
        context = {
            'menu': Food.objects.filter(restaurant_id=pk)
        }
        return render(request, "restaurant.html", context)
