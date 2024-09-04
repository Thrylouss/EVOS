from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='', widget=forms.TextInput())
    password1 = forms.CharField(label='', widget=forms.PasswordInput())
    password2 = forms.CharField(label='', widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class LoginForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput())
    password = forms.CharField(label='', widget=forms.PasswordInput())
