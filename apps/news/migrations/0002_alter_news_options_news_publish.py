# Generated by Django 4.1 on 2022-08-17 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'news', 'verbose_name_plural': 'news'},
        ),
        migrations.AddField(
            model_name='news',
            name='publish',
            field=models.BooleanField(default=True, verbose_name='publish'),
        ),
    ]