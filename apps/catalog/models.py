from django.db import models
from pytils.translit import slugify


class Category(models.Model):
    title = models.CharField('title', max_length=255, blank=False)
    slug = models.SlugField('slug', max_length=255, blank=True, null=True, unique=True)
    publish = models.BooleanField('publish', default=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return f'/{self.slug}/'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Products(models.Model):
    category = models.ForeignKey(Category, related_name='category_products', on_delete=models.CASCADE)
    title = models.CharField('title', max_length=255)
    slug = models.SlugField('slug', max_length=255, blank=True, null=True, unique=True)
    description = models.TextField('description', null=True)
    price = models.IntegerField('price', default=0)
    image = models.ImageField('image', upload_to='images/products/', default='images/products/no_image.jpg', blank=True)
    publish = models.BooleanField('publish', default=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Products, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
