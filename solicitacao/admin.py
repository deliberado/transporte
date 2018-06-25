from django.contrib import admin
from .models import *


admin.site.register(Funcionario)
admin.site.register(Solicitacao)
admin.site.register(Atendimento)
admin.site.register(Veiculo)

