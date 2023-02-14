from django.forms import ModelForm
from django import forms
from .models import User


class LogInForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Username', 'class': 'form-input'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password', 'class': 'form-input'}))


class SignUpForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}), min_length=8)
    confirmPassword = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm password'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'phoneNumber')
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
                    "placeholder": "Phone number",
                    "type": "tel",
                }
            ),
        }

    def clean_password(self):
        cd = self.cleaned_data
        if (cd['password'] != cd['confirmPassword']):
            raise forms.ValidationError('Passwords dont match')
        return cd['confirmPassword']
    # username = forms.CharField(widget=forms.TextInput(
    #     attrs={'placeholder': 'Username'}))
    # email = forms.EmailField(widget=forms.EmailInput(
    #     attrs={'placeholder': 'Email'}))
    # phoneNumber = forms.CharField(widget=forms.TextInput(
    #     attrs={'placeholder': 'Phone number', 'type': 'tel'}))
