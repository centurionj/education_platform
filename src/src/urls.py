from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('users/', include('users.urls')),
    path('courses/', include('courses.urls')),
#     path('favourites/', include('favourites.urls')),
#     path('testing/', include('testing.urls')),
]
