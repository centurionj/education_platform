from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from common.views import TitleMixin
from users.forms import UserRegistrationForm
from users.models import User


class UserRegistrationView(TitleMixin, SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('dashboard')
    success_message = 'Вы успешно зарегестрированы!'
    title = 'Регистрация'


def login(request):
    return render(request, 'users/singin.html')


def dashboard(request):
    return render(request, 'users/dashboard.html')


def setups(request):
    return render(request, 'users/settings.html')
