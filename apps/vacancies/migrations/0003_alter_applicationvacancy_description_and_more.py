# Generated by Django 4.1 on 2022-09-19 10:14

import apps.base.services
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0002_alter_applicationvacancy_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationvacancy',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='applicationvacancy',
            name='docs',
            field=models.FileField(blank=True, null=True, upload_to='vacancies/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['txt', 'pdf', 'doc', 'docx']), apps.base.services.validate_size_file], verbose_name='docs'),
        ),
    ]
