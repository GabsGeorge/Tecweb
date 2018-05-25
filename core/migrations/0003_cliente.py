# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-05-09 19:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180509_1556'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('cpf', models.IntegerField(db_column='CPF', unique=True)),
                ('telefone_u', models.IntegerField(db_column='Telefone_U')),
                ('endereco_u', models.CharField(db_column='Endereco_U', max_length=255)),
                ('news', models.NullBooleanField(db_column='News')),
            ],
            options={
                'abstract': False,
            },
            bases=('core.usuario',),
        ),
    ]
