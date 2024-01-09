from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView

from common.views_mixin import TitleMixin
from courses.models import Category, Course
from users.models import User
from users.enums import RoleStatuses


class IndexView(TitleMixin, ListView):
    """Отображение индексной стр"""
    template_name = 'main/index.html'
    title = 'Главная'
    queryset = Course.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        courses = Course.objects.all()
        categories = Category.objects.all()
        teachers = User.objects.filter(role=RoleStatuses.TEACHER)

        context['courses'] = courses
        context['categories'] = categories
        context['teachers'] = teachers
        return context


class ContactsView(TemplateView):
    """Страница с контактами"""
    template_name = 'main/contacts.html'


def coming_soon(request):
    """Страница заглушка"""
    return render(request, 'main/coming_soon.html')
