from django.urls import path
from .views import (
    CatalogAPIView, CatalogCategoryAPIView, ProductAPIView)


urlpatterns = [
    path('catalog/', CatalogAPIView.as_view(), name='category'),
    path('catalog/<str:slug_category>/', CatalogCategoryAPIView.as_view(), name='category-product'),
    path('catalog/<str:slug_category>/<str:slug_product>/', ProductAPIView.as_view(), name='product'),
]
