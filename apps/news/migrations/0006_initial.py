# Generated by Django 4.1 on 2022-08-17 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('news', '0005_delete_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='slug')),
                ('small_text', models.TextField(verbose_name='small_text')),
                ('big_text', models.TextField(verbose_name='big_text')),
                ('image', models.ImageField(blank=True, default='images/news/no_image.jpg', upload_to='images/news/', verbose_name='image')),
                ('date', models.DateField(auto_now_add=True, verbose_name='date')),
                ('publish', models.BooleanField(default=True, verbose_name='publish')),
                ('item_url', models.URLField(unique=True)),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
