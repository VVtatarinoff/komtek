from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.

class RefTitles(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Имя справочника')
    short_name = models.CharField(max_length=50, unique=True, verbose_name='Короткое имя справочника')
    description = models.TextField(verbose_name='Описание справочника')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Глобальные справочники'
        verbose_name_plural = 'Глобальные справочники'
        ordering = ['id']


class RefVersions(models.Model):
    reference = models.ForeignKey(RefTitles, on_delete=models.RESTRICT,
                                  verbose_name='глобальный справочник')
    version = models.CharField(max_length=50, verbose_name='Версия справочника')
    init_date = models.DateField(verbose_name='Дата начала действия')

    def __str__(self):
        return self.version

    def save(self, *args, **kwargs):
        same_name = RefVersions.objects.filter(reference_id=self.reference_id, version=self.version)
        if same_name:
            raise ValidationError(
                {'version': "Не может быть одинаковых версий для одного справочника"})
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Версии справочников'
        verbose_name_plural = 'Версии справочников'
        ordering = ['id']


class Elements(models.Model):
    ref_version = models.ForeignKey(RefVersions, on_delete=models.RESTRICT,
                                    verbose_name='версия справочника')
    code = models.CharField(max_length=150, verbose_name='Код элемента')
    value = models.CharField(max_length=150, verbose_name='Значение элемента')

    class Meta:
        verbose_name = 'Элементы справочника'
        verbose_name_plural = 'Элементы справочника'
        ordering = ['id']
