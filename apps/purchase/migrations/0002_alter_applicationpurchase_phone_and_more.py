# Generated by Django 4.1 on 2022-09-20 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationpurchase',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='phone'),
        ),
        migrations.AlterField(
            model_name='applicationpurchase',
            name='tick',
            field=models.BooleanField(verbose_name='tick'),
        ),
    ]
