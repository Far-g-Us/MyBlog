from django import forms
from .models import Article

class ArticleUserProfileForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['image_profile', 'first_name', 'last_name', 'age', 'about_me']