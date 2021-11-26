from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    data_nascimento =models.DateField()
    responsavel = models.CharField(max_length=100)
    telefone_responsavel = models.CharField(max_length=11)
    data_inclusao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nome
    
