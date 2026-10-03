from django.db import models

class Servicos(models.Model):
    descricao = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.descricao


class Clientes(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    cpf = models.CharField(max_length=14)

    def __str__(self):
        return self.nome
# Create your models here.
