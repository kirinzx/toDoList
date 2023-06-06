from django import forms
from django.forms import ModelForm
from .models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate, login as auth_login

class LogInForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Username', 'class': 'form-input'}), required=True)
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password', 'class': 'form-input'}), required=True)
    
    def __init__(self, request, *args, **kwargs):
        self.request = request
        super().__init__(*args, **kwargs)

    def clean(self, **kwargs):
        cleaned_data = super(LogInForm, self).clean()
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        authShot = authenticate(username=username,password=password)
        if not authShot:
            self.add_error(None,"Incorrect username or password")
        else:
            auth_login(self.request,authShot)
        return cleaned_data

class SignUpForm(ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={"placeholder": "Password","class":"form-input"}))
    password2 = forms.CharField(
        label='Confirm password', widget=forms.PasswordInput(attrs={"placeholder": "Confirm password", "class":"form-input"}))
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'phoneNumber', 'password')
        widgets = {
            "username": forms.TextInput(
                attrs={
                    "placeholder": "Username",
                    "class":"form-input"
                }
            ),
            "first_name": forms.TextInput(
                attrs={
                    "placeholder": "First name",
                    "class":"form-input"
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "placeholder": "Last name",
                    "class":"form-input"
                }
            ),
            "email": forms.TextInput(
                attrs={
                    "placeholder": "Email",
                    "class":"form-input"
                }
            ),
            "phoneNumber": forms.TextInput(
                attrs={
                    "placeholder": "Phone number (with a country code) ",
                    "type": "tel",
                    "minlength": 12,
                    "maxlength": 12,
                    "class":"form-input"
                },
            ),
        }
    def clean_password(self):
        password1 = self.cleaned_data.get('password')
        try:
            validate_password(password1, self.instance)
        except forms.ValidationError as error:
            self.add_error('password', error)
        return password1
    
    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("password2")
        if password and confirm_password:
            if password != confirm_password:
                self.add_error(None, "Passwords don't match")
        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user