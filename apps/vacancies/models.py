from django.db import models
from django.core.validators import FileExtensionValidator

from apps.base.services import validate_size_file


class Vacancy(models.Model):
    title = models.CharField('Название вакансии', max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вакансию'
        verbose_name_plural = 'Вакансии'


class ApplicationVacancy(models.Model):
    fullname = models.CharField('Имя', max_length=255)
    vacancy = models.CharField('Вакансия', max_length=100)
    email = models.EmailField('Email', max_length=50)
    phone = models.CharField('Телефон', max_length=20)
    description = models.TextField('Описание', blank=True, null=True)
    docs = models.FileField('Документ', upload_to='vacancies/', blank=True, null=True,
                            validators=[FileExtensionValidator(allowed_extensions=['txt', 'pdf', 'doc', 'docx']),
                                        validate_size_file])

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = 'Заявку на вакансию'
        verbose_name_plural = 'Заявки на вакансии'
