# Generated by Django 4.1.4 on 2022-12-28 12:18

import apps.base.services
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0005_alter_applicationvacancy_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applicationvacancy',
            old_name='name',
            new_name='fullname',
        ),
        migrations.AlterField(
            model_name='applicationvacancy',
            name='docs',
            field=models.FileField(default=1, upload_to='vacancies/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['txt', 'pdf', 'doc', 'docx']), apps.base.services.validate_size_file], verbose_name='Документ'),
            preserve_default=False,
        ),
    ]
