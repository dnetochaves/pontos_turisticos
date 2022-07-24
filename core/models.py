from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentarios
from endereco.models import Endereco

class PontosTuristicos(models.Model):
    nome = models.CharField(max_length=150, null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao, blank=True, null=True)
    comentarios = models.ManyToManyField(Comentarios, blank=True, null=True)
    enderecos = models.ForeignKey(Endereco, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
