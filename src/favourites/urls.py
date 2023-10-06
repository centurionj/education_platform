from django.urls import path
from . import views

urlpatterns = [
    # path('', views.CatalogView.as_view(), name='catalog'),
    path('favourites/<int:course_id>/', views.favourite_add, name='favourites_update'),
]
