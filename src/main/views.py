from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView

from common.views import TitleMixin
from courses.models import Category, Course
from users.models import User


class IndexView(TitleMixin, ListView):
    """Отображение индексной стр"""
    template_name = 'main/index.html'
    title = 'Главная'

    def get_queryset(self):
        return Course.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        courses = Course.objects.all()
        categories = Category.objects.all()
        teachers = [user for user in User.objects.all() if user.is_teacher()]

        context['courses'] = courses
        context['categories'] = categories
        context['teachers'] = teachers
        return context


class ContactsView(TemplateView):
    template_name = 'main/contacts.html'


def coming_soon(request):
    return render(request, 'main/coming_soon.html')