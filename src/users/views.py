from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from common.views import TitleMixin
from users.forms import UserRegistrationForm, UserLogingForm
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


def setups(request):
    return render(request, 'users/settings.html')
