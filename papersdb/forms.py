from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import Author, Paper
from django import forms

class PaperForm(ModelForm):
    
    class Meta:
        model = Paper
        # fields = exclude
        exclude = ('notes',)