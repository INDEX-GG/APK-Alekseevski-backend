# Generated by Django 4.1 on 2022-08-25 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_products_description_alter_products_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='publish',
            field=models.BooleanField(verbose_name='publish'),
        ),
    ]
