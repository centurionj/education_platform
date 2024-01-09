from django.urls import path

from . import views


urlpatterns = [
    path('favourites/<int:user_id>/', views.FavouriteListView.as_view(), name='favourites'),
    path('favourites/add_or_delete/<int:course_id>/', views.add_or_delete, name='favourites_update'),
]
