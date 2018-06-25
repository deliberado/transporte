from django.contrib import admin
from django.urls import path

from solicitacao.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="pagina_inicial"),
    path('autenticar/', do_login, name="autenticar"),
    path('veiculos/', lista_veiculos, name="lista_veiculos"),
    path('veiculos/add', criar_veiculo, name='criar_veiculo'),
    path('motoristas/', lista_motoristas, name="lista_motoristas"),
    path('motoristas/add', criar_motorista, name='criar_motorista'),
]
