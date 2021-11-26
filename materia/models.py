from django.db import models

# Create your models here.
class Materia(models.Model):
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=3)
    data_inclusao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nome