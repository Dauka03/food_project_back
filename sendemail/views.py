from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from config.settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL

# Create your views here.
def contact_view(request):
    if request.method == "GET":
        form = ContactForm()
    elif request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(f'{full_name} от {from_email}', 
                message, 
                DEFAULT_FROM_EMAIL,
                [DEFAULT_FROM_EMAIL], 
                RECIPIENTS_EMAIL)
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
            return redirect('success')
    else:
        return HttpResponse('Неверный запрос.')
    return render(request,"contact.html",{'form': form})
def success_view(request):
    return HttpResponse("Приняли! Спасибо за вашку заявку.")  
