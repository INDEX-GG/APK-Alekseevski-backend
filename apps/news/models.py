from django.db import models
from pytils.translit import slugify


class News(models.Model):
    title = models.CharField('title', max_length=255)
    description = models.TextField('description')
    text = models.TextField('text')
    image = models.ImageField('image', upload_to='images/news/')
    date = models.DateField('date', auto_now_add=True)

    def __str__(self):
        return self.title

    def src(self):
        return self.image.url

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
