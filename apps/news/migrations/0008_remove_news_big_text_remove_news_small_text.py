# Generated by Django 4.1 on 2022-08-18 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_remove_news_item_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='big_text',
        ),
        migrations.RemoveField(
            model_name='news',
            name='small_text',
        ),
    ]
