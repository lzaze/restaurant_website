from django.shortcuts import render
from django.http import JsonResponse
import json

from .models import Food, Restaurant, Order, OrderItem


def home_view(request):
    context = {
        'res': Restaurant.objects.all()
    }
    return render(request, "home.html", context)


def restaurant_view(request, pk):
    context = {
        'menu': Food.objects.filter(restaurant_id=pk)
    }
    return render(request, "restaurant.html", context)


def update_item(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('Product Id:', productId)

    customer = request.user.customer
    product = Food.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item added', safe=False)
