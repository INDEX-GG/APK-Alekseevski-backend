from django.db import models
from django.core.validators import FileExtensionValidator
from apps.base.services import validate_size_file


class Vacancy(models.Model):
    title = models.CharField('title', max_length=255)
    description = models.TextField('description')
    text = models.TextField('text')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вакасния'
        verbose_name_plural = 'Вакансии'


class ApplicationVacancy(models.Model):
    name = models.CharField('name', max_length=255)
    vacancy = models.ForeignKey(Vacancy, related_name='application_vacancy', on_delete=models.CASCADE)
    email = models.EmailField('email', max_length=50)
    phone = models.CharField('phone', max_length=20)
    description = models.TextField('description', blank=True, null=True)
    docs = models.FileField('docs',
                            upload_to='vacancies/',
                            blank=True,
                            null=True,
                            validators=[FileExtensionValidator(allowed_extensions=['txt', 'pdf', 'doc', 'docx']),
                                        validate_size_file])

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Заявка на вакансию'
        verbose_name_plural = 'Заявки на вакансии'
