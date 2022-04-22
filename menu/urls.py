from unicodedata import name
from django.contrib import admin
from django.urls import path

from .models import Picture
from . import views
from .views import HomeView, PictureListView


app_name='menu'

urlpatterns = [
    path('', views.HomeView.as_view(), name="Home"),
    path('<slug:slug>/',views.FoodPostListView.as_view(),name="foodPost_list"),
    path('data-json/', views.PictureListView.as_view(), name='data-json'),
    path('shipping', views.shipping, name='shipping'),

]