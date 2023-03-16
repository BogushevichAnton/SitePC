from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User


# Register your models here.

class UserCreationForm(forms.ModelForm):
    email = forms.CharField(label='E-mail',
                            widget=forms.EmailInput())

    first_name = forms.CharField(label='Имя', widget=forms.TextInput())
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput())
    date_of_birth = forms.DateTimeField(label='Дата рождения', input_formats=['%d.%m.%Y'], widget=forms.DateInput())
    mobile = forms.CharField(error_messages={"unique": "Уже есть пользователь с таким номером телефона."},
                             label='Номер телефона', widget=forms.TextInput())
    address = forms.CharField(label='Адрес', widget=forms.TextInput())
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = (
        'email', 'first_name', 'last_name', 'date_of_birth', 'mobile', 'address', 'password1', 'password2', 'is_active',
        'is_superuser', 'is_staff')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    email = forms.CharField(label='E-mail',
                            widget=forms.EmailInput())

    first_name = forms.CharField(label='Имя', widget=forms.TextInput())
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput())
    date_of_birth = forms.DateTimeField(label='Дата рождения', input_formats=['%d.%m.%Y'], widget=forms.DateInput(
        attrs={'class': 'form-control form-input', 'data-toggle': 'datepicker',
               'placeholder': 'Дата рождения'}))
    mobile = forms.CharField(error_messages={"unique": "Уже есть пользователь с таким номером телефона."},
                             label='Номер телефона', widget=forms.TextInput())
    address = forms.CharField(label='Адрес', widget=forms.TextInput())
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(), required=False)
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(), required=False)

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'date_of_birth', 'mobile', 'address', 'is_active',
                  'is_superuser', 'is_staff', 'is_active', 'password1', 'password2')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        user = super(UserChangeForm, self).save(commit=False)
        if password1 != '' and password2 != '' and password1 == password2:
            user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'first_name', 'last_name', 'date_of_birth', 'mobile', 'address', 'password1', 'password2'),
        }),
        ('Permissions', {'fields': ('is_superuser', 'is_staff', 'is_active')}),

    )
    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'password', 'first_name', 'last_name', 'date_of_birth', 'mobile', 'address', 'password1',
                'password2'),
        }),
        ('Permissions', {'fields': ('is_superuser', 'is_staff', 'is_active')}),
    )

    list_display = ('email', 'date_joined', 'mobile')
    search_fields = ('email', 'mobile')
    filter_horizontal = ()
    list_filter = ()
    ordering = ('email',)


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
