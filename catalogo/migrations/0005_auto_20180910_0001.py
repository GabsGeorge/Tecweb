# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-09-10 03:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0004_auto_20180910_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(blank=True, db_column='Imagem', null=True, upload_to='media', verbose_name='Imagem'),
        ),
    ]
