from msilib.schema import ListView
from unicodedata import category
from django.shortcuts import render
from django.views.generic import ListView

from menu.models import foodPost

# Create your views here.


class FoodPostListView(ListView):
    model = foodPost

    def get_queryset(self):
        return foodPost.objects.filter(category__slug=self.kwargs.get('slug'))


def home(request):
    return render(request, 'index.html')
