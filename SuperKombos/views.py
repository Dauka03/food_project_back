from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

def index(request):
    return HttpResponse("SuperKombos will make you happy and full always!")


def categories(request):
    return HttpResponse("<h1>SuperKombos, Pizzas with toppings, hamburgers and fries are up to you.</h1>")

def changes(request,size):
    if int(size)>3:
        raise Http404() #redirect('/', permanent=True)

    return HttpResponse(f"<h1>Resizing the meal</h1><p>{size}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Oops, something went wrong...</h1>')
