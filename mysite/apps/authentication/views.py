from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as auth_login, authenticate, logout
from .forms import LogInForm, SignUpForm
from rest_framework import generics
from rest_framework.authtoken.models import Token
from django.contrib.auth.password_validation import validate_password
from .serializers import TokenSerializer


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def login(request):
    if not request.user.is_authenticated:
        logInForm = LogInForm(request)
        if is_ajax(request=request):
            logInForm = LogInForm(request,request.POST)
            if logInForm.is_valid():
                return JsonResponse({'success': "Вход был успешно выполнен"})
            else:
                return JsonResponse({'errors': logInForm.errors})
        return render(request, 'logIn.html', {"form": logInForm})
    else:
        return redirect("home")

def logout_view(request):
    logout(request)
    return redirect('login')

def signUp(request):
    if not request.user.is_authenticated:
        signUpForm = SignUpForm()
        if is_ajax(request=request):
            signUpForm = SignUpForm(request.POST)
            if signUpForm.is_valid():
                user = signUpForm.save()
                user.save()
                auth_login(request, user)
                return JsonResponse({'success': "Аккаунт был успешно создан"})
            else:
                return JsonResponse({'errors': signUpForm.errors})
        return render(request, 'signUp.html', {"form": signUpForm})
    else:
        return redirect('home')
class UserTokenView(generics.RetrieveAPIView):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer
    lookup_field = 'user_id'