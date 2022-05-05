from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/(<slug_id>\d+)/', views.cart_add, name='cart_add'),
    path('remove/(<slug_id>\d+)/', views.cart_remove, name='cart_remove'),
]
