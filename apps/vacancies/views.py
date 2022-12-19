from rest_framework import viewsets
from apps.base.permissions import IsAdminOrReadOnly
from .serializers import VacancySerializer, ApplicationVacancySerializer
from .models import Vacancy, ApplicationVacancy


class VacancyViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    permission_classes = (IsAdminOrReadOnly,)


class ApplicationVacancyViewSet(viewsets.ModelViewSet):
    queryset = ApplicationVacancy.objects.all()
    serializer_class = ApplicationVacancySerializer
    permission_classes = (IsAdminOrReadOnly,)
