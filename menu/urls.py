from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('<slug:slug>/',views.FoodPostListView.as_view(),name="foodPost_list")
]