from django.urls import path

from reguser.views import loginuserView
from .views import PopularArticlesListView, homeView

urlpatterns = [
    path('', homeView, name='home'),
    path('popular-articles/', PopularArticlesListView, name='popular_articles'),
]