# Generated by Django 4.1.4 on 2022-12-29 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0016_news_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='address',
            field=models.TextField(blank=True, null=True, verbose_name='Адрес'),
        ),
    ]