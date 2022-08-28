from django import forms
from .models import Hava

class ListForm(forms.ModelForm):
    class Meta:
        model = Hava
        fields = ["day","date","derece","description", "sehir"]