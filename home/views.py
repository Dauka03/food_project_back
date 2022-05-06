from django.shortcuts import render
from msilib.schema import ListView
from django.views.generic import ListView, DetailView
# Create your views here.


def home(request):
    return render(request, 'menu/home.html')