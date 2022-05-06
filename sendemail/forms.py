# sendemail/forms.py
from django import forms

class ContactForm(forms.Form):
    full_name = forms.CharField(label='name', required=True)
    from_email = forms.EmailField(label='email', required=True)
    message = forms.CharField(label='message', widget=forms.Textarea, required=True)