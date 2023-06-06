from django.urls import path
from . import views

urlpatterns = [
    path('vkLink', views.vkLink,name='vk'),
]