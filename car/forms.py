from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import News

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Add email field

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

# forms.py

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, label='Search')


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content']

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
        