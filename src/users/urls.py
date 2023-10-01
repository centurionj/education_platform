from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.UserRegistrationView.as_view(), name='registration'),
    # path('product/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('setups/', views.setups, name='setups'),
]
