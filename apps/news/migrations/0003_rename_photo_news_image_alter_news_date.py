# Generated by Django 4.1 on 2022-08-17 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_news_options_news_publish'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='photo',
            new_name='image',
        ),
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateField(auto_now_add=True, verbose_name='date'),
        ),
    ]