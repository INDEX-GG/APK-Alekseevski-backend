# Generated by Django 4.1 on 2022-08-23 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bidding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
                ('text', models.TextField(verbose_name='text')),
                ('image', models.ImageField(blank=True, default='images/bidding/no_image.jpg', upload_to='images/bidding/', verbose_name='image')),
                ('docs', models.FileField(blank=True, default='docs/bidding/no_docs.pdf', upload_to='docs/bidding/', verbose_name='docs')),
            ],
            options={
                'verbose_name': 'Торги',
                'verbose_name_plural': 'Торги',
            },
        ),
    ]
