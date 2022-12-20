from django.urls import path

from apps.purchase import views

urlpatterns = [
    path('purchase/', views.PurchaseAPIView.as_view()),
    path('purchase/<int:pk>/', views.PurchaseItemAPIView.as_view()),
]
