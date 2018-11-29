from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import UserRegistrationForm


# Create your views here.

def login_user(request):

    if request.method == "POST":
        username = request.POST.get('user')
        password = request.POST.get('password')
        print(request.POST)
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('professor:list_prof')
        else:
            messages.error(request, 'Bad user name or passwrod')
    return render(request, 'index.html')

def logout_user(request):
    logout(request)
    return redirect('professor:list_prof')

def user_registration(request):
    data = {}
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        print(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, password=password)
            #messages.success(request, 'usuario cdastrado {}'.format(user.username))
            return redirect('profiles:login')
    else:
        form = UserRegistrationForm()

    data['form'] = form
    return render(request, 'profiles/register.html', data)