from django import forms
from .models import ShortURL

class ShortURLForm(forms.ModelForm):
    
    org_url = forms.URLField(widget=forms.URLInput(
        attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Enter URL to shorten'
        }
    ))
    
    class Meta:
        model = ShortURL
        fields = ['org_url',]