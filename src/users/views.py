from django.contrib.auth.views import LoginView, PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

from common.views import TitleMixin
from users.forms import (
    UserChangePasswordForm,
    UserEditForm,
    UserLogingForm,
    UserRegistrationForm,
)
from users.models import User


class UserRegistrationView(TitleMixin, SuccessMessageMixin, CreateView):
    """регистрация пользователя"""
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('dashboard')
    success_message = 'Вы успешно зарегестрированы!'
    title = 'Регистрация'


class UserLoginView(TitleMixin, LoginView):
    """вход пользователя на сайте"""
    template_name = 'users/singin.html'
    form_class = UserLogingForm
    title = 'Авторизация'


def dashboard(request):
    return render(request, 'users/dashboard.html')


class UserUpdateView(TitleMixin, UpdateView):
    """Обновление информации о пользователе"""
    template_name = 'users/settings.html'
    model = User
    form_class = UserEditForm
    title = 'Настройки'

    def get_success_url(self):
        return reverse_lazy('setups', kwargs={'pk': self.object.pk})


class UserChangePasswordView(UserUpdateView, PasswordResetView):
    """Смена пароля пользователем"""

    form_class = UserChangePasswordForm
