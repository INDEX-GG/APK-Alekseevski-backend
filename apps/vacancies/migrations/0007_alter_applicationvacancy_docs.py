# Generated by Django 4.1.4 on 2022-12-28 12:39

import apps.base.services
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0006_rename_name_applicationvacancy_fullname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationvacancy',
            name='docs',
            field=models.FileField(blank=True, null=True, upload_to='vacancies/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['txt', 'pdf', 'doc', 'docx']), apps.base.services.validate_size_file], verbose_name='Документ'),
        ),
    ]
