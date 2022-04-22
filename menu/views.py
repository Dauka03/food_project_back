from msilib.schema import ListView
from unicodedata import category
from django.shortcuts import render
from django.views.generic import ListView, TemplateView, View
from django.core import serializers
from .models import foodPost, Picture
from django.http import JsonResponse
from .models import *
# Create your views here.

class FoodPostListView(ListView):
    model = foodPost
    
    def get_queryset(self):
        return foodPost.objects.filter(category__slug=self.kwargs.get('slug'))



def home(request):
    return render(request, 'index.html')

class HomeView(TemplateView):
    template_name = "menu/picture_list.html"

class PictureListView(ListView):
    def get(self,request):
        qs = Picture.objects.all()
        data = serializers.serialize('json',qs)
        return JsonResponse({'data':data}, safe=False)

def shipping(request): 
    return render(request, 'menu/shipping.html')
