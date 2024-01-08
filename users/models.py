from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)
    observacao = models.TextField()
    idade = models.IntegerField()
