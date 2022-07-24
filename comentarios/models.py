from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Comentarios(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    comentario = models.TextField(null=True, blank=True)
    data = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    aprovado = models.BooleanField(default=True, null=True, blank=True)

    def __str__(self):
        return self.comentario
