from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apps.news import views


urlpatterns = [
    path('', views.NewsList.as_view()),
    path('<int:pk>/', views.NewsDetail.as_view()),
]