from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import FileResponse, Http404

from courses.models import Course
from . models import Lecture


class LectureListView(ListView):
    model = Lecture
    template_name = 'lectures/lectures.html'
    context_object_name = 'lectures'

    def get_queryset(self):
        queryset = super(LectureListView, self).get_queryset()
        course_slug = self.kwargs.get('course_slug')
        return queryset.filter(course__slug=course_slug) if course_slug else queryset


class LectureDetailView(DetailView):
    model = Lecture
    template_name = 'lectures/lecture_detail.html'
    context_object_name = 'lecture'

    def get_object(self, queryset=None):
        course_slug = self.kwargs.get('course_slug')
        lecture_slug = self.kwargs.get('lecture_slug')
        return Lecture.objects.get(course__slug=course_slug, slug=lecture_slug)
