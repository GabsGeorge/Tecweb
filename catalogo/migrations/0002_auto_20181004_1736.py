# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-04 20:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='peso',
            field=models.DecimalField(db_column='peso', decimal_places=2, default=1, max_digits=10, verbose_name='Peso'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produto',
            name='qtd_de_itens',
            field=models.SmallIntegerField(db_column='Quantidade de Itens', default=1, verbose_name='Quantidade de itens'),
            preserve_default=False,
        ),
    ]
