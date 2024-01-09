from django.views.generic import DetailView
from django.views.generic.list import ListView

from common.views import TitleMixin

from .models import News


class NewsListView(TitleMixin, ListView):
    """Отображение всех новостей на странице"""
    title = 'Новости'
    model = News
    template_name = 'news/news_list.html'
    context_object_name = 'news'
    paginate_by = 8


class NewsDetailView(DetailView):
    """Детальный просмотр новости"""
    model = News
    template_name = 'news/news_detail.html'
    context_object_name = 'news'
