# Generated by Django 2.2.11 on 2021-04-13 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Имя')),
                ('phone', models.CharField(max_length=16, verbose_name='Телефон')),
                ('comment', models.TextField(blank=True, max_length=1024, verbose_name='Комментарий')),
            ],
            options={
                'verbose_name': 'клиента',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Вид', max_length=128, verbose_name='Название')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Цена')),
                ('link', models.CharField(default='url', max_length=128, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'цену',
                'verbose_name_plural': 'Цены',
                'ordering': ('id',),
            },
        ),
    ]
