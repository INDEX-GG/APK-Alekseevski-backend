# Generated by Django 4.1 on 2022-12-19 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_products_publish'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default=1, upload_to='images/category/', verbose_name='image'),
            preserve_default=False,
        ),
    ]