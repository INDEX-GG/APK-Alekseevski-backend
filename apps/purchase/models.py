from django.db import models


class Purchase(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    description = models.TextField('Краткое описание')
    text = models.TextField('Полный текст')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Закупку'
        verbose_name_plural = 'Закупки'


class DocsSamples(models.Model):
    purchase_docs_samples = models.ForeignKey(Purchase, on_delete=models.CASCADE, related_name='purchase_docs_samples')
    docs = models.FileField('Образец заявки', upload_to='docs/purchase/')

    def src_docs(self):
        return self.docs.url

    class Meta:
        verbose_name = 'Образец заявки'
        verbose_name_plural = 'Образец заявки'


class Docs(models.Model):
    purchase_docs = models.ForeignKey(Purchase, on_delete=models.CASCADE, related_name='purchase_docs')
    docs = models.FileField('Документ о закупках', upload_to='docs/purchase/')

    def src_docs(self):
        return self.docs.url

    class Meta:
        verbose_name = 'Документы о закупках'
        verbose_name_plural = 'Документы о закупках'


class Images(models.Model):
    purchase_images = models.ForeignKey(Purchase, on_delete=models.CASCADE, related_name='purchase_images')
    image = models.ImageField('Картинка', upload_to='images/purchase/')

    def src_image(self):
        return self.image.url

    class Meta:
        verbose_name = 'Картинки'
        verbose_name_plural = 'Картинки'


class ApplicationPurchase(models.Model):
    inn = models.CharField('inn', max_length=255)
    organization = models.CharField('organization', max_length=255)
    email = models.EmailField('email', max_length=255)
    phone = models.CharField('phone', max_length=20)
    tick = models.BooleanField('tick')

    def __str__(self):
        return self.organization

    class Meta:
        verbose_name = 'Заявка на закупку'
        verbose_name_plural = 'Заявки на закупку'
