from django.contrib import admin
from core.models import *

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Food)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)