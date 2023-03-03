from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from .models import *

User = get_user_model()


# Берем Register и закидываем на него UserChangeForm
class RegisterUserForm(UserCreationForm):
    email = forms.CharField(error_messages={"unique": "Уже есть пользователь с таким e-mail."}, label='E-mail',
                            widget=forms.EmailInput(
                                attrs={'class': 'form-control form-control-lg form-input', 'placeholder': 'E-mail'}))

    first_name = forms.CharField(label='Имя', widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg form-input', 'placeholder': 'Имя'}))

    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg form-input', 'placeholder': 'Фамилия'}))

    date_of_birth = forms.DateTimeField(label='Дата рождения', input_formats=['%d.%m.%Y'], widget=forms.DateInput(
        attrs={'class': 'form-control form-control-lg form-input', 'data-toggle': 'datepicker',
               'placeholder': 'Дата рождения'}))

    mobile = forms.CharField(error_messages={"unique": "Уже есть пользователь с таким номером телефона."},
                             label='Номер телефона', widget=forms.TextInput(
            attrs={'class': 'form-control form-control-lg form-input', 'placeholder': 'Номер телефона'}))

    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-control form-control-lg form-input', 'placeholder': 'Пароль'}))

    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(
        attrs={'class': 'form-control form-control-lg form-input', 'placeholder': 'Повтор пароля'}))

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'date_of_birth', 'mobile', 'password1', 'password2')


class AuthUserForm(AuthenticationForm):
    username = UsernameField(label='E-mail', widget=forms.EmailInput(
        attrs={"autofocus": True, 'class': 'form-control form-control-lg form-input', 'placeholder': 'E-mail'}))

    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-control form-control-lg form-input', 'placeholder': 'Пароль'}))


class UserUpdateForm(UserChangeForm):
    email = forms.CharField(error_messages={"unique": "Уже есть пользователь с таким e-mail адресом."},
                            label='E-mail',
                            widget=forms.EmailInput(
                                attrs={'class': 'form-control'}
                            ))

    first_name = forms.CharField(label='Имя', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    date_of_birth = forms.DateTimeField(label='Дата рождения', input_formats=['%d.%m.%Y'], widget=forms.DateInput(
        attrs={'class': 'form-control form-input', 'data-toggle': 'datepicker',
               'placeholder': 'Дата рождения'}))
    mobile = forms.CharField(error_messages={"unique": "Уже есть пользователь с таким номером телефона."},
                             label='Номер телефона', widget=forms.TextInput(
            attrs={'class': 'form-control'}
        ))
    address = forms.CharField(label='Адрес', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ), required=False)
    password = None

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email', 'date_of_birth', 'mobile', 'address')
