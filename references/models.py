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
        if not self.version:
            raise ValidationError(
                {'version': 'поле не может быть пустым'})
        return super().save(*args, **kwargs)

    class Meta:
        unique_together = [['reference', 'version'], ['reference', 'init_date']]
        verbose_name = 'Версии справочников'
        verbose_name_plural = 'Версии справочников'
        ordering = ['id']


class Elements(models.Model):
    ref_version = models.ForeignKey(RefVersions, on_delete=models.RESTRICT,
                                    verbose_name='версия справочника')
    code = models.CharField(max_length=150, verbose_name='Код элемента')
    value = models.CharField(max_length=150, verbose_name='Значение элемента')

    def save(self, *args, **kwargs):
        if not self.code:
            raise ValidationError(
                {'code': 'поле не может быть пустым'})
        if not self.value:
            raise ValidationError(
                {'value': 'поле не может быть пустым'})
        return super().save(*args, **kwargs)

    class Meta:
        unique_together = ['ref_version', 'code']
        verbose_name = 'Элементы справочника'
        verbose_name_plural = 'Элементы справочника'
        ordering = ['id']
