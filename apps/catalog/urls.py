from django.urls import path
from . import views

urlpatterns = [
    path('catalog/', views.CatalogAPIView.as_view(), name='catalog'),
    path('catalog/<str:slug>/', views.CatalogCategoryAPIView.as_view(), name='catalog-category'),
    path('catalog/<str:slug>/<str:slug_p>/', views.ProductAPIView.as_view(), name='product'),
]
