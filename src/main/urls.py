from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('product/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
    # path('parsing/', views.parsing, name='parsing'),
    # path('fill_bd/', views.fill_bd, name='fill_bd')
]
