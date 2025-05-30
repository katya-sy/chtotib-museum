# Generated by Django 5.2 on 2025-04-25 06:34

import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_article_content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeperiod',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='time_period/images/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='mainpagecontent',
            name='description',
            field=django_ckeditor_5.fields.CKEditor5Field(max_length=1000, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='section',
            name='description',
            field=django_ckeditor_5.fields.CKEditor5Field(max_length=255, verbose_name='Описание раздела'),
        ),
        migrations.AlterField(
            model_name='traditionimage',
            name='image',
            field=models.ImageField(upload_to='traditions/images/', verbose_name='Изображение'),
        ),
    ]
