from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True, error_messages={'unique':"This username has already been registered."})
    password = models.CharField(max_length=200, unique=False)
    email = models.EmailField(unique=True, error_messages={'unique':"This email has already been registered."})
    phoneNumber = models.CharField(max_length=12, unique=True, error_messages={'unique':"This phone number has already been registered."})
    is_staff = models.BooleanField(default=False)
    def __str__(self):
        return self.username
    
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)