# Generated by Django 4.0.3 on 2022-03-31 15:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0007_alter_refversions_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elements',
            name='code',
            field=models.SlugField(max_length=100, validators=[django.core.validators.MinLengthValidator(4)], verbose_name='Код элемента'),
        ),
        migrations.AlterField(
            model_name='reftitles',
            name='description',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(4)], verbose_name='Описание справочника'),
        ),
        migrations.AlterField(
            model_name='reftitles',
            name='name',
            field=models.SlugField(unique=True, validators=[django.core.validators.MinLengthValidator(4)], verbose_name='Имя справочника'),
        ),
        migrations.AlterField(
            model_name='reftitles',
            name='short_name',
            field=models.CharField(max_length=50, unique=True, validators=[django.core.validators.MinLengthValidator(4)], verbose_name='Короткое имя справочника'),
        ),
        migrations.AlterField(
            model_name='refversions',
            name='version',
            field=models.SlugField(validators=[django.core.validators.MinLengthValidator(4)], verbose_name='Версия справочника'),
        ),
    ]
