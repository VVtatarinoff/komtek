# Generated by Django 4.0.3 on 2022-03-31 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0004_alter_refversions_init_date'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='refversions',
            unique_together={('reference', 'version'), ('reference', 'init_date')},
        ),
    ]
