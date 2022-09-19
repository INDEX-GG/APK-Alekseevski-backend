from rest_framework import viewsets
from apps.base.permissions import IsAdminOrReadOnly
from . import serializers
from . import models


class VacancyViewSet(viewsets.ModelViewSet):
    queryset = models.Vacancy.objects.all()
    serializer_class = serializers.VacancySerializer
    permission_classes = (IsAdminOrReadOnly,)


class ApplicationVacancyViewSet(viewsets.ModelViewSet):
    queryset = models.ApplicationVacancy.objects.all()
    serializer_class = serializers.ApplicationVacancySerializer
    # permission_classes = (IsAdminOrReadOnly,)
