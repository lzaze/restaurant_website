from django.urls import path

from .views import HomeView, RestaurantView

urlpatterns = [
    path('', HomeView.as_view(), name='home-page'),
    path('restaurant/<int:pk>/', RestaurantView.as_view(), name='restaurant')
]
