from django.db import models


class News(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    description = models.TextField('Краткое описание')
    text = models.TextField('Полное описание')
    address = models.TextField('Адрес', blank=True, null=True)
    image = models.ImageField('Изображение', upload_to='images/news/', default='images/no_image.jpg')
    date = models.DateField('Дата', auto_now_add=True)

    def __str__(self):
        return self.title

    def src(self):
        return self.image.url

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
