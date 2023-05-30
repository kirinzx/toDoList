from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as auth_login,authenticate, logout
from .forms import LogInForm, SignUpForm



def login(request):
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
                return redirect('login')
    else:
        form = LogInForm()
    return render(request, 'logIn.html', {"form": form})


def logout_view(request):
    logout(request)
    return redirect('login')

def signUp(request):
    
    if (request.method == 'POST'):
        form = SignUpForm(request.POST)
        if (form.is_valid()):
            user = form.save(commit=False)
            user.set_password('password')
            user.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signUp.html', {"form": form})
