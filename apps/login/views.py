from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
# from django import forms
from .forms import RegistrationForm, LoginForm
from .models import User
import bcrypt

# Create your views here.
def index(request):
    loginForm = LoginForm()
    registrationForm = RegistrationForm()
    context = {
        'loginForm': loginForm,
        'registrationForm': registrationForm
    }
    return render(request, 'login/login.html', context)

def login(request):
    if request.method=='POST':
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            response = User.objects.filter(email = request.POST['email'])
            request.session['user_name'] = response[0].first_name
            request.session['user_id'] = response[0].id
            return redirect(reverse('beltexam:index'))
        else:
            registrationForm = RegistrationForm()
            context = {'loginForm': loginForm, 'registrationForm': registrationForm}
            return render(request, 'login/login.html', context)
    else:
        loginForm = LoginForm()
        registrationForm = RegistrationForm()
        context = {"loginForm": loginForm, "registrationForm": registrationForm}
        return render(request, 'login/login.html', context)

def registration(request):
    if request.method=='POST':
        registrationForm = RegistrationForm(request.POST)
        loginForm = LoginForm()
        if registrationForm.is_valid():
            newUser = registrationForm.save()
            request.session['user_name'] = newUser.first_name
            request.session['user_id'] = newUser.id
            return redirect(reverse('beltexam:index'))
    else:
        registrationForm = RegistrationForm()
        loginForm = LoginForm()

    context = {"registrationForm": registrationForm, "loginForm": loginForm}
    return render(request, 'login/login.html', context)

def logout(request):
    request.session.flush()
    return redirect(reverse('login:login'))

# def success(request):
#
#     return render(request, 'login/success.html')
