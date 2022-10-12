# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-09-13 13:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problema',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=20, verbose_name='Titulo')),
                ('imagem', models.ImageField(null=True, upload_to='imagens/', verbose_name='Imagem')),
                ('descricao', models.TextField(max_length=200, verbose_name='Descricao')),
                ('respostaCerta', models.CharField(max_length=20, null=True, verbose_name='Resposta Certa')),
            ],
        ),
    ]
