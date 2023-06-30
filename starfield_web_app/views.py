from django.contrib import messages, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.forms import BaseForm
from django.http import HttpRequest
from django.shortcuts import render, redirect
from .forms import SignupForm


# Create your views here.

def form_errors_as_messages(request: HttpRequest, form: BaseForm):
    for field in form.fields:
        for error in field.errors:
            messages.warning(request, error)


def dashboard(request: HttpRequest):
    return render(request, 'dashboard.html')


def signup(request: HttpRequest):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.create_user(username=username, password=password)

        auth.login(request, user)
        return redirect('dashboard')

    return render(request, 'auth/signup.html')


def log_in(request: HttpRequest):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)

        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('profile-page')
        else:
            messages.warning(request, 'Неверный логин и/или пароль')
            return redirect('auth-login')

    return render(request, 'auth/login.html')


def logout_view(request: HttpRequest):
    logout(request)
    return redirect('auth-login')


@login_required
def profile_page(request: HttpRequest):
    context = {
        'user': request.user
    }
    return render(request, 'profile-page.html', context)
