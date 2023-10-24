from django.urls import path
from reguser.views import profileView, profileupView
from .views import PopularArticlesListView, homeView, search

urlpatterns = [
    path('', homeView, name='home'),
    path('profile/', profileView, name='profile'),
    path('profileup/', profileupView, name='profileup'),
    path('popular-articles/', PopularArticlesListView, name='popular_articles'),
    path('search/', search, name='search'),
]