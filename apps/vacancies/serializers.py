from rest_framework import serializers

from apps.vacancies.models import Vacancy, ApplicationVacancy


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = '__all__'


class ApplicationVacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationVacancy
        fields = '__all__'
