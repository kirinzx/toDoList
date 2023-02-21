from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True, error_messages={'unique':"This username has already been registered."})
    password = models.CharField(max_length=200, unique=False)
    email = models.EmailField(unique=True, error_messages={'unique':"This email has already been registered."})
    phoneNumber = models.CharField(max_length=12, unique=True, error_messages={'unique':"This phone number has already been registered."})
    is_staff = models.BooleanField(default=False)