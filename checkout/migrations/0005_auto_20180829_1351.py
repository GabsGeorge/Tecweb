# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-08-29 16:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_auto_20180829_1124'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='preco',
            new_name='preco_p',
        ),
    ]