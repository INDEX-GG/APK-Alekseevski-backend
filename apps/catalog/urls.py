from django.urls import path

from apps.catalog.views import CategoryAPIView, CategoryItemAPIView, ProductAPIView


urlpatterns = [
    path('catalog/', CategoryAPIView.as_view()),
    path('catalog/<str:slug_category>/', CategoryItemAPIView.as_view(),),
    path('catalog/<str:slug_category>/<str:slug_product>/', ProductAPIView.as_view()),
]
