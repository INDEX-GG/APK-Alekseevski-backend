from django.contrib import admin
from apps.vacancies.models import Vacancy, ApplicationVacancy

admin.site.register(Vacancy)
admin.site.register(ApplicationVacancy)
