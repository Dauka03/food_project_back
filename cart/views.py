from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from menu.models import Tag
from .cart import Cart
from .forms import CartAddProductForm

# Create your views here.


@require_POST
def cart_add(request, slug_id):
    cart = Cart(request)
    slug = get_object_or_404(Tag, id=slug_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(slug=slug,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, slug_id):
    cart = Cart(request)
    slug = get_object_or_404(Tag, id=slug_id)
    cart.remove(slug)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'orders/detail.html', {'cart': cart})
