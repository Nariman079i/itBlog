from django import forms

from .models import *

class AddPageForm(forms.Form):
    title = forms.CharField(max_length=30)

    description = forms.CharField(widget=forms.Textarea(attrs={'cols':60, 'rows':10}))
    isPublished = forms.BooleanField()
    isOpen = forms.BooleanField()
    lesson_int = forms.IntegerField()
