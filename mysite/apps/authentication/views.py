from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as auth_login, logout
from .forms import LogInForm, SignUpForm
from rest_framework import generics
from rest_framework.authtoken.models import Token
from .serializers import TokenSerializer
from apps.authentication.models import User
import requests
from urllib import parse
import random
import string

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def login(request):
    code = request.GET.get('code')
    if code:
        response = requests.get('https://oauth.vk.com/access_token?' + parse.urlencode({
            'client_id': '	51668968',
            'client_secret': '2yPZGBvcluZvAU5VKRqj',
            'redirect_uri': 'http://127.0.0.1:8000/login',
            'code': code,
        })).json()

        email = response.get('email')

        responseData = requests.get('https://api.vk.com/method/users.get?' + parse.urlencode({
            'user_ids': response.get('user_id'),
            'fields': 'photo_max_orig,first_name,last_name,screen_name',
            'v': 5.131,
        }),headers={
            'Authorization': f'Bearer {response.get("access_token")}'
        }).json()
        if 'response' in responseData:
            response2 = responseData.get('response')[0]
            first_name = response2.get('first_name')
            last_name = response2.get('last_name')
            username = response2.get('screen_name')
            photoUrl = response2.get('photo_max_orig')

            photoResponse = requests.get(photoUrl)

            def fileNameGenerator(size, chars=string.ascii_uppercase + string.digits):
                return ''.join(random.choice(chars) for _ in range(size))
            
            if email and not (User.objects.filter(email=email).exists() or User.objects.filter(username=username).exists()):
                fileName = fileNameGenerator(10)
                with open(f'media/images/usersPhoto/{fileName}.png','wb')as file:
                    file.write(photoResponse.content)
                newUser = User.objects.create(
                    username=username,
                    first_name = first_name,
                    last_name = last_name,
                    email = email,
                    password = '',
                    photo = f'images/usersPhoto/{fileName}.png',
                )
                auth_login(request,newUser)
            else:
                if email:
                    auth_login(request,User.objects.get(email=email))
                else:
                    return redirect('login')
            return redirect('home')

    if not request.user.is_authenticated:
        logInForm = LogInForm(request)
        if is_ajax(request=request):
            logInForm = LogInForm(request, request.POST)
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
