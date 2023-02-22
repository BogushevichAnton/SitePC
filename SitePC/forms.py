from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget = forms.TextInput(attrs={'class': 'form-control form-control-lg form-input',  'placeholder': 'Логин'}))
    password1 = forms.CharField(label='Пароль', widget = forms.PasswordInput(attrs={'class': 'form-control form-control-lg form-input',  'placeholder': 'Пароль'}))
    password2 = forms.CharField(label='Повтор пароля',widget = forms.PasswordInput(attrs={'class': 'form-control form-control-lg form-input',  'placeholder': 'Повтор пароля'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
