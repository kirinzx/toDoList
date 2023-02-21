from django.forms import ModelForm, ValidationError
from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


class LogInForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Username', 'class': 'form-input'}), required=True)
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password', 'class': 'form-input'}), required=True, min_length=8)


class SignUpForm(ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={"placeholder": "Password"}), min_length=8)
    password2 = forms.CharField(
        label='Confirm password', widget=forms.PasswordInput(attrs={"placeholder": "Confirm password"}), min_length=8)

    class Meta:
        model = User
        fields = ('username', 'email', 'phoneNumber', 'password')
        widgets = {
            "username": forms.TextInput(
                attrs={
                    "placeholder": "Username"
                }
            ),
            "email": forms.TextInput(
                attrs={
                    "placeholder": "Email"
                }
            ),
            "phoneNumber": forms.TextInput(
                attrs={
                    "placeholder": "Phone number (with a country code) ",
                    "type": "tel",
                    "minlength": 12,
                    "maxlength": 12,
                },
            ),
        }

    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("password2")
        if password and confirm_password:
            if password != confirm_password:
                self.add_error(None, "Passwords don't match")
        return cleaned_data

    def checkIfExist(self):
        cleaned_data = super(SignUpForm, self).clean()
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")
        phoneNumber = self.cleaned_data.get("phoneNumber")
        if User.objects.filter(email.exists()):
            self.add_error('email', "That email already exists")
        if User.objects.filter(username.exists()):
            self.add_error('username', "That username already exists")
        if User.objects.filter(phoneNumber.exists()):
            self.add_error('phoneNumber', "That phone number already exists")
        return cleaned_data
