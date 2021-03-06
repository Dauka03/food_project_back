from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.MenuListView.as_view(),name="menu"),
    path('<slug:slug>/',views.FoodPostListView.as_view(),name="foodPost_list"),
    path('<slug:slug>/<slug:foodPost_slug>/',views.FoodPostDetailView.as_view(), name="foodPost_single")
]