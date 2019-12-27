# -*- coding: utf-8 -*-
from django.db import models


class SeoConfiguration(models.Model):
    bool = models.BooleanField('Активность', default=True)
    name = models.CharField('Название', default='Услуга', max_length=128)
    price = models.PositiveIntegerField('Цена', default=0)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'настройку SEO'
        verbose_name_plural = 'Настройки SEO'
        ordering = ('id',)