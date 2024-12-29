from django import forms
from .models import Cartoon

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Cartoon
        fields = ['image', 'description']
