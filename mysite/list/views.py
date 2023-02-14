from django.shortcuts import render
from .forms import LogInForm, SignUpForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.


def login(request):
    if (request.method == 'POST'):
        form = LogInForm(request.POST)
        if (form.is_valid()):
            return render(request, 'toDoList.html')
    else:
        logInForm = LogInForm()
        return render(request, 'logIn.html', {"form": logInForm})


@login_required
def profile(request):
    return render(request, 'profile.html')


@login_required
def toDoList(request):
    return render(request, 'toDoList.html')


def signUp(request):
    if (request.method == 'POST'):
        form = SignUpForm(request.POST)
        if (form.is_valid()):
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return render(request, 'toDoList.html')
    else:
        signUpForm = SignUpForm()
        return render(request, 'signUp.html', {"signUpForm": signUpForm})
