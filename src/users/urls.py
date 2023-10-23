from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views


urlpatterns = [
    path('registration/', views.UserRegistrationView.as_view(), name='registration'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/', views.DashboardListView.as_view(), name='dashboard'),
    path('setups/<int:pk>/', views.UserUpdateView.as_view(), name='setups'),
    path('reset_password/<int:pk>', views.UserChangePasswordView.as_view(), name='reset_password'),
    path('delete_image/', views.delete_image, name='delete_image'),
    path('dashboard_redirect/', views.login_redirect, name='dashboard_redirect'),
]
