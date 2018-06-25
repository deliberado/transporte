from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html', context={})

def do_login(request):
    return render(request, 'login.html')

@login_required
def lista_veiculos(request):
    lista_veiculos = Veiculo.objects.all()
    return render(request, 'lista_veiculos.html', context={'lista_veiculos':lista_veiculos})

def criar_veiculo(request):
    return render(request, 'veiculo_add.html', context=None)

def lista_motoristas(request):
    lista_motoristas = Funcionario.objects.all()
    return render(request, 'lista_motoristas.html', context={'lista_motoristas':lista_motoristas})

def criar_motorista(request):
    lista_usuarios = User.objects.all()
    return render(request, 'motorista_add.html', context={'lista_usuarios': lista_usuarios})