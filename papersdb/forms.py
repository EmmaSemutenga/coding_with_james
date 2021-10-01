from django import forms
from django.db.models import fields
# from django.forms import ModelForm, Form
from .models import Author, Paper

class PaperForm(forms.ModelForm): # What is in brackets here is inherited.
    
    class Meta: # Meta is a class that is "data about data"
        model = Paper
        # fields = exclude
        exclude = ('notes',) # tuples must have a trailing comma

#class AuthorForm(forms.Form): here you're representing the parent class form, and then adding extra features, here on line 13.
#    author_name = forms.CharField(max_length=50) In models.py, we have this line basically, so better to delete due to DRY.
# This code on lines 13-14 is for the long way.

class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ('name',)
