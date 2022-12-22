from django.db import models


class Addresses(models.Model):
    title = models.CharField('Адрес', max_length=255, blank=False)
    geotag = models.TextField('Метка', blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'


class Video(models.Model):
    video = models.FileField('Видео', upload_to='video/', null=True)

    def src(self):
        return self.video.url

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'
