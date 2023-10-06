from django.views.generic import DetailView
from django.views.generic.list import ListView

from common.views import TitleMixin

from .models import Category, Course
from favourites.models import CourseLike


class CourseListView(TitleMixin, ListView):
    """отображение всех курсов"""
    model = Course
    template_name = 'courses/catalog.html'
    paginate_by = 6
    title = 'Каталог'

    def get_queryset(self):
        queryset = super(CourseListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CourseListView, self).get_context_data()
        context['categories'] = Category.objects.all()
        return context


class CourseDetailView(DetailView):
    """Детальный просмотр курса"""
    model = Course
    template_name = 'courses/course_detail.html'
    context_object_name = 'course'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        """Определяем контекст для курса, курсов этой категории и преподов к курсу"""
        context = super().get_context_data(**kwargs)
        course = context[self.context_object_name]
        similar_courses = Course.objects.filter(category=course.category).exclude(pk=course.pk)
        instructor = course.teacher
        context['similar_courses'] = similar_courses
        context['instructor'] = instructor
        return context
