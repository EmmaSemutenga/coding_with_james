from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import Author, Paper
from django import forms
from django.contrib import admin

class PaperForm(ModelForm):
    
    
    class Meta:
        model = Paper
        # fields = exclude
        exclude = ('notes',)
        widgets = {
            'authors' : forms.CheckboxSelectMultiple
        }
        

# class PaperAdminForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(PaperAdminForm, self).__init__(*args, **kwargs)
#         self.fields['authors'].widget = admin.widgets.AdminCheckboxWidget()