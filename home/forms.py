from django import forms
from .models import Arta

class ArtaUserProfileForm(forms.ModelForm):
    class Meta:
        model = Arta
        fields = ['image_profile', 'first_name', 'last_name', 'age', 'about_me']