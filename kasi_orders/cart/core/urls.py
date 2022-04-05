from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from users import views as user_views

urlpatterns = [
    path('', views.home_view, name='home-page'),
    path('restaurant/<int:pk>/', views.restaurant_view, name='restaurant'),
    path('update_item/', views.update_item, name='update-item'),
    path('cart/', views.cart_view, name='cart'),
    path('profile/', user_views.profile, name='profile'),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]
