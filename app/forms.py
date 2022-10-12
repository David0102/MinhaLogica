from django import forms
from .models import Problema

class ProblemaForm(forms.ModelForm):
    class Meta:
        model = Problema
        fields = '__all__'