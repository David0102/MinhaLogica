# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import this
from unittest.util import _MAX_LENGTH

from django.db import models

# Create your models here.

class Problema(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length = 20, null = True, verbose_name = "Titulo")
    imagem = models.ImageField(upload_to = 'imagens/', null = True, verbose_name = "Imagem")
    descricao = models.TextField(max_length = 200, verbose_name = "Descricao")
    respostaCerta = models.CharField(max_length = 20, null = True, verbose_name = "Resposta Certa")

    def __str_(self):
        titulo = "Titulo" + self.titulo
        return titulo
