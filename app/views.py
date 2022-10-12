# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from multiprocessing import context
from pickle import NONE
from random import random, randrange
from re import X

from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProblemaForm
from .models import Problema
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.
def index(request):
    return render(request, "index.html")

def login(request):
    return render(request, "login.html")

def submeterProblema(request):
    form = ProblemaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('perfil')
    return render(request, "submeter.html", {'form': form})

def cadastro(request):
    return render(request, "submeter.html")
@login_required
def painel(request):
    id = randrange(4,7)
    print(id)
    problema = Problema.objects.all()
    context = {
        'problema': problema,
        'id': id
    }
    return render(request, "painel.html", context)

def perfil(request):
    problemas = Problema.objects.all()
    return render(request, "perfil.html", {'problemas': problemas})

def editar(request, id):
    if request.method == 'GET':
        problemas = Problema.objects.all()
        problema = Problema.objects.filter(id = id).first()
        form = ProblemaForm(instance = problema)
        context={
            'problemas':problemas,
            'form': form
        }
        return render(request, "editar.html", context)
    elif request.method == 'POST':
        #problemas = Problema.objects.all()
        problema = Problema.objects.filter(id = id).first()
        form = ProblemaForm(request.POST , request.FILES, instance = problema)
        if form.is_valid():
            form.save()
            return redirect('perfil')
        else:
            problemas: Problema.objects.all()
        context={
            'problemas':problemas,
            'form': form
        }
        return render(request, "editar.html", context)
    #return render(request, "editar.html")

def excluir(request, id):
    problema = Problema.objects.get(id = id)
    problema.delete()
    return redirect('perfil')

class SingUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = ('registration/register.html')