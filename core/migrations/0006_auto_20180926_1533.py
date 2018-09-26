# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-26 18:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_usuario_second_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='usuario_ptr',
        ),
        migrations.AddField(
            model_name='cliente',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='cpf',
            field=models.IntegerField(db_column='CPF', default=1, unique=True, verbose_name='CPF'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='endereco_u',
            field=models.CharField(db_column='Endereco_U', default=1, max_length=255, verbose_name='Endereço'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='news',
            field=models.NullBooleanField(db_column='News', verbose_name='Deseja receber novidades ?'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='telefone_u',
            field=models.IntegerField(db_column='Telefone_U', default=1, verbose_name='Telefone'),
            preserve_default=False,
        ),
    ]
