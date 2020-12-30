from django import forms
from .models import *

class FileInputForm(forms.ModelForm):
    class Meta:
        model = FileInput
        fields = ['key', 'file', 'choice']
