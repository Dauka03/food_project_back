from msilib.schema import ListView
from multiprocessing import context
from unicodedata import category
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView

from menu.models import Tag, foodPost
from cart.forms import CartAddProductForm


# Create your views here.


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


def product_detail(request, id, slug):
    product = get_object_or_404(Tag,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'detail.html', {'slug': slug,
                                           'cart_product_form': cart_product_form})
