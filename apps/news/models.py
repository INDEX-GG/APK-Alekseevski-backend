from django.db import models
from django.urls import reverse_lazy
from django.conf import settings
from django.template.defaultfilters import slugify


class News(models.Model):
    title = models.CharField('title', max_length=255)
    slug = models.SlugField('slug', max_length=255, blank=False, unique=True)
    # description
    small_text = models.TextField('small_text')
    big_text = models.TextField('big_text')
    image = models.ImageField('image', upload_to='images/news/', default='images/news/no_image.jpg', blank=True)
    date = models.DateField('date', auto_now_add=True)
    publish = models.BooleanField('publish', default=True)

    # item_url = models.URLField(unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def get_absolute_url(self):
        return reverse_lazy('product', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
