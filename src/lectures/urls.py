from django.urls import path

from . import views


urlpatterns = [
    path('courses/<slug:course_slug>/lectures/', views.LectureListView.as_view(), name='course_lectures'),
]
