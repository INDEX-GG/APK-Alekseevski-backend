from django.urls import path

from apps.vacancies import views

urlpatterns = [
    path('vacancy/', views.VacancyAPIView.as_view()),
    path('vacancy/application/', views.ApplicationVacancyAPIView.as_view()),
]
