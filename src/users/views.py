from django.contrib.auth.views import LoginView, PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.shortcuts import HttpResponseRedirect, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView

from common.views import TitleMixin
from courses.models import Course
from users.forms import (
    UserChangePasswordForm,
    UserEditForm,
    UserLogingForm,
    UserRegistrationForm,
)
from users.models import User


def login_redirect(request):
    if request.user.is_authenticated:
        if request.user.is_student():
            return redirect(reverse('dashboard'))
        return redirect(reverse('admin:index'))


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


class DashboardListView(TitleMixin, ListView):
    """Отображение всех курсов в личном кабинете"""
    model = Course
    template_name = 'users/dashboard.html'
    paginate_by = 5
    context_object_name = 'courses'
    title = 'Личный кабинет'

    def get_queryset(self):
        user = self.request.user
        course_filter = Q(groups__user_groups=user)
        return Course.objects.filter(course_filter)


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
        return form_class(user=self.request.user)


def delete_image(request):
    """Удаление фотки профиля"""

    image = request.user.image
    image.delete()
    return HttpResponseRedirect(reverse_lazy('setups', kwargs={'pk': request.user.pk}))
