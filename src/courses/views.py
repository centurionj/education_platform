from django.views.generic.list import ListView

from common.views import TitleMixin
from . models import Course, Category


class CourseListView(TitleMixin, ListView):
    """отображение всех курсов"""
    model = Course
    template_name = 'courses/catalog.html'
    paginate_by = 2
    title = 'Каталог'

    def get_queryset(self):
        queryset = super(CourseListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CourseListView, self).get_context_data()
        context['categories'] = Category.objects.all()
        return context
