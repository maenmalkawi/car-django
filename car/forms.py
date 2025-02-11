from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Add email field

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class carForms(forms.ModelForm):
    class Meta:
        model = Car
        fields ='__all__'
        widgets = {
            'dateOfIndustry':forms.DateInput(attrs={'type':'date'}),
        }
        
        


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        