from django.db import models

# Create your models here.
class Atracao(models.Model):
    nome = models.CharField(max_length=150, null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)
    horario_funcionamento = models.TextField(null=True, blank=True)
    idade_minima = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.nome