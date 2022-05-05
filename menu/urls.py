from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('<slug:slug>/', views.FoodPostListView.as_view(), name="foodPost_list"),
]
