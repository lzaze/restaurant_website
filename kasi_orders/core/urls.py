from django.urls import path
from django.contrib.auth import views as auth_views

from .views import HomeView, RestaurantView
from users import views as user_views

urlpatterns = [
    path('', HomeView.as_view(), name='home-page'),
    path('restaurant/<int:pk>/', RestaurantView.as_view(), name='restaurant'),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]
