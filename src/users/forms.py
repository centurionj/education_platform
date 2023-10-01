from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

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
        'class': 'form-control border-0 bg-light rounded-end ps-1', 'placeholder': 'Пароль'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=True)
        return user


class UserLogingForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control border-0 bg-light rounded-end ps-1', 'placeholder': 'Имя пользователя'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control border-0 bg-light rounded-end ps-1', 'placeholder': 'Пароль'
    }))

    class Meta:
        model = User
        fields = ('username', 'password')
