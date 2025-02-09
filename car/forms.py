from django import forms
from .models import *

class carForms(forms.ModelForm):
    class Meta:
        model = Car
        fields ='__all__'
        widgets = {
            'dateOfIndustry':forms.DateInput(attrs={'type':'date'}),
        }
        
