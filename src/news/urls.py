from django.urls import path

from . import views


urlpatterns = [
    path('', views.NewsListView.as_view(), name='news_list'),
    path('<int:pk>/', views.NewsDetailView.as_view(), name='news_detail'),
]
