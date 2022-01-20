from django import forms
from django.forms import ModelForm
from .models import info

class InfoForm(ModelForm):
    	class Meta:
            model = info
            fields = ['name', 'email', 'message']
            