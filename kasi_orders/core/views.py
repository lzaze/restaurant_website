from django.shortcuts import render
from django.http import JsonResponse
import json

from .models import Food, Restaurant, Order, OrderItem


def home_view(request):
    """Home view"""
    context = {
        'res': Restaurant.objects.all(),
    }
    return render(request, "home.html", context)


def restaurant_view(request, pk):
    """A view for restaurants"""
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_total
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']

    context = {
        'menu': Food.objects.filter(restaurant_id=pk),
        'cartItems': cartItems
    }
    return render(request, "restaurant.html", context)


def cart_view(request):
    """Cart view"""

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {
        'items': items,
        'order': order,
    }
    return render(request, "cart.html", context)


def update_item(request):
    """Updates cart items"""
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

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
