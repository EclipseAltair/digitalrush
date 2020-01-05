# -*- coding: utf-8 -*-
from django.db import models


class Client(models.Model):
    name = models.CharField('Имя', max_length=32, blank=False)
    phone = models.CharField('Телефон', max_length=16, blank=False)
    comment = models.TextField('Комментарий', max_length=1024, blank=True)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'клиента'
        verbose_name_plural = 'Клиенты'

class Price(models.Model):
    name = models.CharField('Название', default='Вид', max_length=128)
    price = models.PositiveIntegerField('Цена', default=0)
    link = models.CharField('Ссылка', default='url', max_length=128)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'цену'
        verbose_name_plural = 'Цены'
        ordering = ('id',)
