from django.db import models


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
    description = models.TextField('description')
    docs = models.FileField('docs', upload_to='vacancies/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заявка на вакансию'
        verbose_name_plural = 'Заявки на вакансии'
