from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    observacao = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    telefone = models.CharField(max_length=10)
