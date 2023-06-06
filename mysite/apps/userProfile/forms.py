from django import forms
from apps.authentication.models import User


class PhotoForm(forms.Form):
    photo = forms.ImageField()
