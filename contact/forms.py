from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email','subject','message']
        widgets = {

        }


class SubscribeForm(forms.Form):
    S_email = forms.CharField(label='',widget=forms.EmailInput)