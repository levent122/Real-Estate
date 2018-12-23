from django.shortcuts import render, redirect
from .form import RegisterForm , LoginFrom
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages

def Register(request):

    form = RegisterForm(request.POST or None)

    if form.is_valid():

        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')

        newUser = User(first_name= first_name, last_name= last_name, username= email, email= email)
        newUser.set_password(password)
        newUser.save()

        login(request, newUser)
        return redirect('index')

    context = {
        'form':form
    }

    return render(request, 'user/register.html', context)



def Login(request):

    form = LoginFrom(request.POST or None)

    context = {
        'form':form
    }

    if form.is_valid():

        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')

        user = authenticate(username= email, password= password)

        login(request, user)
        return redirect('index')

    return render(request, 'user/login.html', context)



def Logout(request):
    logout(request)
    return redirect('index')