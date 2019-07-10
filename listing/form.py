from django import forms
from . models import Listing

class ListForm(forms.ModelForm):
    class Meta:
        model = Listing
