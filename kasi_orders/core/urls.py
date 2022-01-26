from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from users import views as user_views

urlpatterns = [
    path('', views.home_view, name='home-page'),
    path('restaurant/<int:pk>/', views.restaurant_view, name='restaurant'),
    path('register/', user_views.register, name='register'),
    path('update_item/', views.update_item, name='update-item'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]
