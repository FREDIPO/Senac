from django.db import models

# Create your models here.
class Pessoas(models.Model):
    CPF = models.CharField(max_length=150)
    NOME = models.CharField(max_length=100)
    NASCIMENTO = models.IntegerField()