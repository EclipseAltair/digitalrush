from django.db import models


class CatalogConfiguration(models.Model):
    bool = models.BooleanField(default=True, verbose_name="Активность")
    name = models.CharField(default='Услуга', max_length=128, verbose_name="Название")
    price = models.PositiveIntegerField(default=0, verbose_name="Цена")

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'настройку сайта-каталога'
        verbose_name_plural = 'Настройки Сайта-каталога'
        ordering = ('id',)
