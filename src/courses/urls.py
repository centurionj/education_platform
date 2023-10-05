from django.urls import path

from . import views


urlpatterns = [
    path('', views.CourseListView.as_view(), name='catalog'),
    path('course/<slug:slug>/', views.CourseDetailView.as_view(), name='course_detail'),
    # path('parsing/', views.parsing, name='parsing'),
    # path('fill_bd/', views.fill_bd, name='fill_bd')
]
