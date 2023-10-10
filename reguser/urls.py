from django.urls import path
from .views import *

urlpatterns = [
    path('register/', reguserView, name='reguser'),
    path('login/', loginuserView, name='loginuser'),
    path('logout/', logoutView, name='logout'),
    path('profile/', profileView, name='profile'),
    path('profileup/', profileupView, name='profileup'),
]
