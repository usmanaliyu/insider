from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import Profile

class UserRegistrationForm(UserCreationForm):


    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()
    image = forms.ImageField()


    class Meta:
        model = User
        fields = ['username','image','first_name','last_name','email']




