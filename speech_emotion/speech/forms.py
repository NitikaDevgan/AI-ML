from django import forms
from .models import SpeechFile

class SpeechFileForm(forms.ModelForm):
    class Meta:
        model = SpeechFile
        fields = ['file']
