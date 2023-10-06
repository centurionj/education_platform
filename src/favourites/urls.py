from django.urls import path

from . import views


urlpatterns = [
    path('favourites/<int:user_id>/', views.FavouriteListView.as_view(), name='favourites'),
    path('favourites/add/<int:course_id>/', views.favourite_add, name='favourites_update'),
]
