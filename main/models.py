# -*- coding: utf-8 -*-
from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=32, null=False, blank=False, verbose_name='Имя')
    phone = models.CharField(max_length=12, null=False, blank=False, verbose_name='Телефон')

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'клиента'
        verbose_name_plural = 'Клиенты'

class Price(models.Model):
    name = models.CharField(default='Вид', max_length=128, verbose_name="Название")
    price = models.PositiveIntegerField(default=0, verbose_name="Цена")
    link = models.CharField(default='url', max_length=128, verbose_name="Ссылка")

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'цену'
        verbose_name_plural = 'Цены'
        ordering = ('id',)
