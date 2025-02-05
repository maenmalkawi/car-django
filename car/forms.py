from django import forms
from .models import *

class carForms(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['CarModel','dateOfIndustry','Engine','gearBox','Wheel']
        widgets = {
            'dateOfIndustry':forms.DateInput(attrs={'type':'date'}),
        }
        
