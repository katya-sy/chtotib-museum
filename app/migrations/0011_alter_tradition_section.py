# Generated by Django 5.2 on 2025-05-12 16:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_section_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tradition',
            name='section',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='app.section', verbose_name='Раздел'),
        ),
    ]
