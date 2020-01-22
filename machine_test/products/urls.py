from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('', views.api_root),
    path('category/', 
        views.CategoryList.as_view(), 
        name='category-list'),
    path('category/<int:pk>/', 
        views.CategoryDetail.as_view(), 
        name='category-detail'),
    path('product/', 
        views.ProductList.as_view(), 
        name='product-list'),
    path('product/<int:pk>/', 
        views.ProductDetail.as_view(), 
        name='product-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
