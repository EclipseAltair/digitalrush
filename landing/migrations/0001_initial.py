# Generated by Django 2.2.3 on 2019-08-18 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LandingConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bool', models.BooleanField(default=True, verbose_name='Активность')),
                ('name', models.CharField(default='Услуга', max_length=128, verbose_name='Название')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'настройку лендинга',
                'verbose_name_plural': 'Настройки Лендинга',
                'ordering': ('id',),
            },
        ),
    ]
