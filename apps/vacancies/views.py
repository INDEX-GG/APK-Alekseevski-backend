from rest_framework import generics

from apps.vacancies.serializers import VacancySerializer, ApplicationVacancySerializer
from apps.vacancies.models import Vacancy, ApplicationVacancy


class VacancyAPIView(generics.ListAPIView):
    queryset = Vacancy.objects.all().order_by('-pk')
    serializer_class = VacancySerializer


class VacancyItemAPIView(generics.RetrieveAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer


class ApplicationVacancyAPIView(generics.CreateAPIView):
    queryset = ApplicationVacancy.objects.all()
    serializer_class = ApplicationVacancySerializer
