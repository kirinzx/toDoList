from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path('profile',views.profile,name='profile'),
]