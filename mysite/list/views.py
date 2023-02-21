from django.forms import ValidationError
from django.shortcuts import render, redirect
from .forms import LogInForm, SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.


def login(request):
    logInForm = LogInForm()
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                username=cd['username'], password=cd['password'])
            if user is not None:
                auth_login(request, user)
                return redirect("home")
            else:
                messages.error(request, "Invalid login or password")
                return render(request, 'logIn.html', {"form": form})
        else:
            logInForm = LogInForm()
            return render(request, 'logIn.html', {"form": form})
    else:
        return render(request, 'logIn.html', {"form": logInForm})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def profile(request):
    return render(request, 'profile.html')


@login_required
def toDoList(request):
    current_user = request.user
    username = current_user.username
    return render(request, 'toDoList.html', {'username': username})


def signUp(request):
    signUpForm = SignUpForm()
    if (request.method == 'POST'):
        form = SignUpForm(request.POST)
        if (form.is_valid()):
            user = form.save(commit=False)
            user.password = make_password('password')
            user.save()
            auth_login(request, user)
            username = user.username
            return render(request, "toDoList.html", {'username': username})
        else:
            return render(request, 'signUp.html', {"form": form})
    else:
        return render(request, 'signUp.html', {"form": signUpForm})
