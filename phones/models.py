from autoslug import AutoSlugField
from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название телефона')
    price = models.FloatField(verbose_name='Цена')
    image = models.URLField(max_length=255, verbose_name='Изображение')
    release_date = models.DateField(verbose_name='Дата выхода')
    lte_exists = models.BooleanField(verbose_name='Наличие LTE версии')
    slug = AutoSlugField(populate_from='name', unique=True, verbose_name='url')

