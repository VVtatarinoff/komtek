# Generated by Django 4.0.3 on 2022-03-30 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RefTitles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Имя справочника')),
                ('short_name', models.CharField(max_length=50, unique=True, verbose_name='Короткое имя справочника')),
                ('description', models.TextField(verbose_name='Описание справочника')),
            ],
            options={
                'verbose_name': 'Глобальные справочники',
                'verbose_name_plural': 'Глобальные справочники',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='RefVersions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=50, verbose_name='Версия справочника')),
                ('init_date', models.DateTimeField(verbose_name='Дата начала действия')),
                ('reference', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='references.reftitles', verbose_name='глобальный справочник')),
            ],
            options={
                'verbose_name': 'Версии справочников',
                'verbose_name_plural': 'Версии справочников',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Elements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=150, verbose_name='Код элемента')),
                ('value', models.CharField(max_length=150, verbose_name='Значение элемента')),
                ('ref_version', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='references.refversions', verbose_name='версия справочника')),
            ],
            options={
                'verbose_name': 'Элементы справочника',
                'verbose_name_plural': 'Элементы справочника',
                'ordering': ['id'],
            },
        ),
    ]
