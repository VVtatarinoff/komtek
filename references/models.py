from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models


# Create your models here.

class RefTitles(models.Model):
    name = models.SlugField(max_length=50, unique=True, verbose_name='Имя справочника', validators=[MinLengthValidator(4)])
    short_name = models.CharField(max_length=50, unique=True, verbose_name='Короткое имя справочника', validators=[MinLengthValidator(4)])
    description = models.TextField(verbose_name='Описание справочника', validators=[MinLengthValidator(4)])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Глобальные справочники'
        verbose_name_plural = 'Глобальные справочники'
        ordering = ['id']


class RefVersions(models.Model):
    reference = models.ForeignKey(RefTitles, on_delete=models.RESTRICT,
                                  verbose_name='глобальный справочник')
    version = models.SlugField(max_length=50, verbose_name='Версия справочника', validators=[MinLengthValidator(4)])
    init_date = models.DateField(verbose_name='Дата начала действия')

    def __str__(self):
        return self.version

    class Meta:
        unique_together = [['reference', 'version'], ['reference', 'init_date']]
        verbose_name = 'Версии справочников'
        verbose_name_plural = 'Версии справочников'
        ordering = ['-init_date']


class Elements(models.Model):
    ref_version = models.ForeignKey(RefVersions, on_delete=models.RESTRICT,
                                    verbose_name='версия справочника')
    code = models.SlugField(max_length=100, verbose_name='Код элемента', validators=[MinLengthValidator(4)])
    value = models.CharField(max_length=150, verbose_name='Значение элемента')

    class Meta:
        unique_together = ['ref_version', 'code']
        verbose_name = 'Элементы справочника'
        verbose_name_plural = 'Элементы справочника'
        ordering = ['id']
