from django.urls import path
from .views import PopularArticlesListView

urlpatterns = [
    path('popular-articles/', PopularArticlesListView.as_view(), name='popular_articles'),
]