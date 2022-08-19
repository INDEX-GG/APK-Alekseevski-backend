from django.db import models
from pytils.translit import slugify


class News(models.Model):
    title = models.CharField('title', max_length=255)
    slug = models.SlugField('slug', max_length=255, blank=True, null=True, unique=True)
    description = models.TextField('description')
    text = models.TextField('text')
    image = models.ImageField('image', upload_to='images/news/', default='images/news/no_image.jpg', blank=True)
    date = models.DateField('date', auto_now_add=True)
    publish = models.BooleanField('publish', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(News, self).save(*args, **kwargs)
