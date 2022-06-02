from django import forms

from .models import *

class AddPageForm(forms.Form):
    title = forms.CharField(max_length=30)
    ico_url = forms.ImageField()
    video_url = forms.FileField()
    description = forms.CharField(widget=forms.Textarea(attrs={'cols':60, 'rows':10}))
    isPublished = forms.BooleanField()
    isOpen = forms.BooleanField()
    lesson_int = forms.IntegerField()
    test_id = forms.ModelChoiceField(queryset=Python.objects.all())