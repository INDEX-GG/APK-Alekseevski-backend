from django.db import models


class Bidding(models.Model):
    title = models.CharField('title', max_length=255)
    description = models.TextField('description')
    text = models.TextField('text')
    image = models.ImageField('image', upload_to='images/bidding/', default='images/bidding/no_image.jpg', blank=True)
    docs = models.FileField('docs', upload_to='docs/bidding/', default='docs/bidding/no_docs.txt', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Торги'
        verbose_name_plural = 'Торги'


class ApplicationBidding(models.Model):
    inn = models.CharField('inn', max_length=255)
    organization = models.CharField('organization', max_length=255)
    email = models.EmailField('email', max_length=255)
    phone = models.CharField('phone', max_length=20, blank=True)
    tick = models.BooleanField('tick', default=False)

    def __str__(self):
        return self.organization

    class Meta:
        verbose_name = 'Заявка на торги'
        verbose_name_plural = 'Заявки на торги'
