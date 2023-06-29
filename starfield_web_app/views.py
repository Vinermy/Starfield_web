from django.contrib import messages, auth
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
        form = SignupForm(request.POST)

        if not form.is_valid():
            form_errors_as_messages(request, form)
            return redirect('auth-signup')

        user = form.save()
        auth.login(request, user)
        return redirect('dashboard')

    return render(request, 'auth/signup.html')
