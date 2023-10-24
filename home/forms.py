from django import forms
from .models import Article, Post

class ArticleUserProfileForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['image_profile', 'first_name', 'last_name', 'age', 'about_me']

class Search(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['name']