from django.db import models
from django.contrib.auth.models import User


class Funcionario(models.Model):
    usuario = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11, verbose_name='CPF')
    matricula = models.IntegerField(verbose_name='matrícula')

    class Meta:
        ordering = ['nome']
        verbose_name = 'Funcionário'

    def __str__(self):
        return self.nome


class Solicitacao(models.Model):
    destino = models.CharField(verbose_name='destino', max_length=200)
    solicitante = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    observacao = models.TextField(blank=True, null=True, verbose_name='observação')
    data_solicitacao = models.DateTimeField(auto_now_add=True, verbose_name='data da solicitação')

    class Meta:
        ordering = ['solicitante__nome']
        verbose_name = 'solicitação'
        verbose_name_plural = 'solicitações'

    def __str__(self):
        return '{id:06d} {solicitante}'.format(
            id=self.id, solicitante=self.solicitante.nome)


class Veiculo(models.Model):
    marca = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200)
    tipo = models.CharField(max_length=200)
    combustivel = models.CharField(max_length=200, verbose_name='combustível')
    placa = models.CharField(max_length=7, unique=True)
    chassi = models.CharField(max_length=17, unique=True)
    ano = models.IntegerField()
    capacidade = models.IntegerField()

    class Meta:
        ordering = ['marca', 'modelo']
        verbose_name = 'veículo'


    def __str__(self):
        return '{} {} {}'.format(self.placa, self.marca, self.modelo)


class Atendimento(models.Model):
    solicitacao = models.OneToOneField(Solicitacao, on_delete=models.CASCADE)
    motorista = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    observacao = models.TextField(blank=True, null=True, verbose_name='observação')
    data_atendimento = models.DateTimeField(blank=True, null=True, verbose_name='data de partida')
    
    def __str__(self):
        return '{}: {}'.format(self.motorista, self.solicitacao)