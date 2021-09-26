from django import forms
from django.db.models import fields
from django.forms import ModelForm, Form
from .models import Author, Paper
from django import forms

class PaperForm(ModelForm): # What is in brackets here is inherited.
    
    class Meta:
        model = Paper
        # fields = exclude
        exclude = ('notes',)

class AuthorForm(Form): # The
    author_name = forms.CharField(max_length=50)

