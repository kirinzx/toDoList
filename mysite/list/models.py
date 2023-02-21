from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=200, unique=False)
    email = models.EmailField(unique=True)
    phoneNumber = models.CharField(max_length=12, unique=True)
    is_staff = models.BooleanField(default=False)