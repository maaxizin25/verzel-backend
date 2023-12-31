from django.db import models
from django.core.validators import MaxValueValidator
from users.models import User

class Announcement(models.Model):
    class Meta:
        ordering = ['id']
    
    TRANSMISSAO_CHOICES = (
        ("M", "Manual"),
        ("A", "Automático")
    )
    
    nome = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    ano = models.IntegerField(
        validators=[MaxValueValidator(9999)]
    )
    valor = models.FloatField()
    km = models.FloatField()
    placa = models.CharField(max_length=7)
    transmissao = models.CharField(max_length=1, choices=TRANSMISSAO_CHOICES)
    cor = models.CharField(max_length=10)
    descricao = models.TextField(max_length=600)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Photos(models.Model):
    class Meta:
        ordering = ['id']

    anuncio = models.ForeignKey(Announcement, on_delete=models.CASCADE, related_name='photos')
    image = models.URLField()