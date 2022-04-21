from msilib.schema import ListView
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from menu.models import foodPost, Category

# Create your views here.
class HomeListView(ListView):
    model = Category
    template_name = "menu/home.html"
class FoodPostListView(ListView):
    model = foodPost
    
    def get_queryset(self):
        return foodPost.objects.filter(category__slug=self.kwargs.get('slug')).select_related('category')

class FoodPostDetailView(DetailView):
    model = foodPost
    slug_url_kwarg = 'foodPost_slug'
    context_object_name = 'post'

def home(request):
    return render(request, 'index.html')