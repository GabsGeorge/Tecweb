# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-11-18 16:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contrato', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataContrato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(verbose_name='Dados do contrato')),
                ('Contrato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contrato.Contrato', verbose_name='Contrato')),
            ],
        ),
    ]