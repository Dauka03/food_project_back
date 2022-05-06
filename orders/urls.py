from django.urls import path
from unicodedata import name
from . import views


urlpatterns = [
    path('create/', views.order_create, name="order_create"),
]
