# Generated by Django 4.0.3 on 2022-03-31 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0006_alter_elements_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='refversions',
            name='version',
            field=models.SlugField(verbose_name='Версия справочника'),
        ),
    ]
