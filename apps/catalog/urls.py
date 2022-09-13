from django.urls import path
from . import views


urlpatterns = [
    path('catalog/', views.CatalogAPIView.as_view(), name='category'),
    path('catalog/<str:slug_category>/', views.CatalogCategoryAPIView.as_view(), name='category-product'),
    path('catalog/<str:slug_category>/<str:slug_product>/', views.ProductAPIView.as_view(), name='product'),
]
