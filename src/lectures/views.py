from django.http import FileResponse, Http404
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from courses.models import Course

from .models import Lecture


class LectureListView(ListView):
    """Отображение лекций на странице"""
    model = Lecture
    template_name = 'lectures/lectures.html'
    context_object_name = 'lectures'

    def get_queryset(self):
        queryset = super(LectureListView, self).get_queryset()
        course_slug = self.kwargs.get('course_slug')
        return queryset.filter(course__slug=course_slug) if course_slug else queryset
