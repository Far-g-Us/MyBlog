from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.db import IntegrityError

from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def reguserView(request):
    if request.method == 'GET':
        return render(request, 'reguser/reguser.html', {'formuser': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.vase()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'reguser/reguser.html', {'formuser': UserCreationForm(), 'error': 'Это имя уже используется'})
        else:
            return render(request, 'reguser/reguser.html', {'formuser': UserCreationForm(), 'error': 'Пароли должны совпадать'})

def loginuserView(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request, 'loginuser/loginuser.html', {'form': form})
    else:
        form = AuthenticationForm()
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        try:
            if user is not None:
                login(request, user)
                return redirect('home')
        except:
            return render(request, template_name='./loginuser/loginuser.html', {'form': form, 'error': 'Неверный логин или пароль'})