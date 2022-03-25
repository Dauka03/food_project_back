from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='home'), #http://127.0.0.1:8000/SuperKombos/ ubrat' pereiti na mysite/urls ubrat' in ''
    path('drinks', categories), #http://127.0.0.1:8000/SuperKombos/categories/
    re_path(r'^changes/(?P<size>[0-9]{1})/', changes),
]
