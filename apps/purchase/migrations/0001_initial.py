# Generated by Django 4.1 on 2022-12-20 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationPurchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inn', models.CharField(max_length=255, verbose_name='inn')),
                ('organization', models.CharField(max_length=255, verbose_name='organization')),
                ('email', models.EmailField(max_length=255, verbose_name='email')),
                ('phone', models.CharField(max_length=20, verbose_name='phone')),
                ('tick', models.BooleanField(verbose_name='tick')),
            ],
            options={
                'verbose_name': 'Заявка на закупку',
                'verbose_name_plural': 'Заявки на закупку',
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Краткое описание')),
                ('text', models.TextField(verbose_name='Полный текст')),
            ],
            options={
                'verbose_name': 'Закупку',
                'verbose_name_plural': 'Закупки',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/purchase/', verbose_name='Картинка')),
                ('purchase_images', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase_images', to='purchase.purchase')),
            ],
            options={
                'verbose_name': 'Картинки',
                'verbose_name_plural': 'Картинки',
            },
        ),
        migrations.CreateModel(
            name='DocsSamples',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docs', models.FileField(upload_to='docs/purchase/', verbose_name='Образец заявки')),
                ('purchase_docs_samples', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase_docs_samples', to='purchase.purchase')),
            ],
            options={
                'verbose_name': 'Образец заявки',
                'verbose_name_plural': 'Образец заявки',
            },
        ),
        migrations.CreateModel(
            name='Docs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docs', models.FileField(upload_to='docs/purchase/', verbose_name='Документ о закупках')),
                ('purchase_docs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase_docs', to='purchase.purchase')),
            ],
            options={
                'verbose_name': 'Документы о закупках',
                'verbose_name_plural': 'Документы о закупках',
            },
        ),
    ]
