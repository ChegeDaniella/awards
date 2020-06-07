from django import forms
from .models import Rates
from django.contrib.auth.models import User

class RateForm(forms.ModelForm):
    class Meta:
        model = Rates
        exclude = ['post','user']