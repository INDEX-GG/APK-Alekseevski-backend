from django.db import models


class Vacancy(models.Model):
    title = models.CharField('title', max_length=255)
    description = models.TextField('description')
    text = models.TextField('text')

    # docs = models.FileField('docs', upload_to='docs/purchase/', default='docs/purchase/no_docs.txt', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вакасния'
        verbose_name_plural = 'Вакансии'


class Vacancy(models.Model):
    title = models.CharField('title', max_length=255)
    description = models.TextField('description')
    text = models.TextField('text')

    # docs = models.FileField('docs', upload_to='docs/purchase/', default='docs/purchase/no_docs.txt', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вакасния'
        verbose_name_plural = 'Вакансии'
