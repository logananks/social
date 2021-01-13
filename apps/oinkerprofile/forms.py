from django import forms
from django.forms import fields

from .models import OinkerProfile

class OinkerProfileForm(forms.ModelForm):
    class Meta:
        model = OinkerProfile
        fields = ('avatar',)