from rest_framework import serializers
from . import models


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vacancy
        fields = '__all__'


class ApplicationVacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ApplicationVacancy
        fields = '__all__'
