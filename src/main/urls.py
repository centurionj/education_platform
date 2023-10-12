from django.urls import path

from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('soon/', views.coming_soon, name='soon')
    # path('product/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
    # path('parsing/', views.parsing, name='parsing'),
    # path('fill_bd/', views.fill_bd, name='fill_bd')
]
