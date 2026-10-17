class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    cpf = models.CharField(max_length=14)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class Servico(models.Model):
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    duracao = models.PositiveIntegerField(help_text='Duração em minutos')
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.descricao


class Agendamento(models.Model):
    class Status(models.TextChoices):
        AGENDADO = 'AGENDADO', 'Agendado'
        REALIZADO = 'REALIZADO', 'Realizado'
        CANCELADO = 'CANCELADO', 'Cancelado'

    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name='agendamentos')
    servico = models.ForeignKey(Servico, on_delete=models.PROTECT, related_name='agendamentos')
    data = models.DateField()
    horario = models.TimeField()
    observacao = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.AGENDADO)

    def __str__(self):
        return f'{self.cliente} - {self.servico} ({self.data} {self.horario})'