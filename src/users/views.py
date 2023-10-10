from django.contrib.auth.views import LoginView, PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import HttpResponseRedirect


from common.views import TitleMixin
from users.forms import (
    UserChangePasswordForm,
    UserEditForm,
    UserLogingForm,
    UserRegistrationForm,
)
from users.models import User


class UserRegistrationView(TitleMixin, SuccessMessageMixin, CreateView):
    """Регистрация пользователя"""

    model = User
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('dashboard')
    success_message = 'Вы успешно зарегестрированы!'
    title = 'Регистрация'


class UserLoginView(TitleMixin, LoginView):
    """Вход пользователя на сайте"""

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

    def get_context_data(self, **kwargs):
        """Для отображения нескольких форм сразу"""

        context = super().get_context_data(**kwargs)
        context['user_edit_form'] = UserEditForm(instance=self.object)
        context['password_change_form'] = UserChangePasswordForm(user=self.object)
        return context

    def get_success_url(self):
        return reverse_lazy('setups', kwargs={'pk': self.object.pk})


class UserChangePasswordView(UserUpdateView, PasswordResetView):
    """Смена пароля пользователем"""

    form_class = UserChangePasswordForm

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(user=self.request.user, **self.get_form_kwargs())


def delete_image(request):
    """Удаление фотки профиля"""

    image = request.user.image
    image.delete()
    return HttpResponseRedirect(reverse_lazy('setups', kwargs={'pk': request.user.pk}))
