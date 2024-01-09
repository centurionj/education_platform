from django.urls import path

from . import views


urlpatterns = [
    path('', views.CourseListView.as_view(), name='catalog'),
    path('course/<slug:slug>/', views.CourseDetailView.as_view(), name='course_detail'),
]
