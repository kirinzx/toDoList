from django.shortcuts import render, redirect
from urllib import parse

def vkLink(request):
    return redirect(
        'https://oauth.vk.com/authorize/?' + parse.urlencode({
            'client_id': '	51668968',
            'client_secret': '2yPZGBvcluZvAU5VKRqj',
            'redirect_uri': 'http://127.0.0.1:8000/login',
            'display': 'page',
            'response_type': 'code',
            'scope': 'email,phone_number',
    }))