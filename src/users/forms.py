from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    UserChangeForm,
    UserCreationForm,
)

from users.models import User


class UserRegistrationForm(UserCreationForm):
    """форма для регистрации"""
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control border-0 bg-light rounded-end ps-1', 'placeholder': 'Имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control border-0 bg-light rounded-end ps-1', 'placeholder': 'Фамилия'}))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control border-0 bg-light rounded-end ps-1', 'placeholder': 'Имя пользователя'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control border-0 bg-light rounded-end ps-1', 'placeholder': 'E-mail'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control border-0 bg-light rounded-end ps-1', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control border-0 bg-light rounded-end ps-1', 'placeholder': 'Подтвердить пароль'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=True)
        return user


class UserLogingForm(AuthenticationForm):
    """Форма для входа в акк"""
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control border-0 bg-light rounded-end ps-1', 'placeholder': 'Имя пользователя'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control border-0 bg-light rounded-end ps-1', 'placeholder': 'Пароль'
    }))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserEditForm(UserChangeForm):
    """Форма для изменений профиля"""
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': '{{user.first_name}}', 'value': '{{user.first_name}}'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control ', 'placeholder': '{{user.last_name}}', 'value': '{{user.last_name}}'}))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': '{{user.username}}', 'value': '{{user.username}}'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'E-mail', '{{user.email}}': '{{user.email}}'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': '{{user.phone_number}}', 'value': '{{user.phone_number}}'}), required=False)
    description = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Описание', 'value': '{{user.description}}'}), required=False)
    image = forms.ImageField(widget=forms.FileInput(attrs={'id': 'uploadfile-1', 'class': 'form-control d-none'}), required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'phone_number', 'description', 'image')

    def save(self, commit=True):
        user = super(UserEditForm, self).save(commit=True)
        return user


class UserChangePasswordForm(PasswordChangeForm):
    """Смена пароля пользователем"""
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Старый пароль'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Новый пароль'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Повторите новый пароль'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

    def save(self, commit=True):
        if self.fields.is_valid():
            user = super(UserChangePasswordForm, self).save(commit=True)
            return user
