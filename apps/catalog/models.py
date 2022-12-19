from django.db import models
from pytils.translit import slugify


class Category(models.Model):
    title = models.CharField('Заголовок', max_length=255, blank=False)
    slug = models.SlugField('slug', max_length=255, blank=True, null=True, unique=True)
    image = models.ImageField('Изображение', upload_to='images/category/')

    def __str__(self):
        return self.title

    def src(self):
        return self.image.url

    """ 
    Automatic formation slug 
    """

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'


class Products(models.Model):
    category = models.ForeignKey(Category, related_name='category_products', on_delete=models.CASCADE)
    title = models.CharField('Заголовок', max_length=255)
    slug = models.SlugField('slug', max_length=255, blank=True, null=True, unique=True)
    description = models.TextField('Описание')
    price = models.IntegerField('Цена')

    def __str__(self):
        return self.title

    """ 
    Automatic formation slug 
    """

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Products, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Images(models.Model):
    products = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField('Картинка', upload_to='images/products/')

    def src(self):
        return self.image.url

    class Meta:
        verbose_name = 'Картинку'
        verbose_name_plural = 'Картинки'
