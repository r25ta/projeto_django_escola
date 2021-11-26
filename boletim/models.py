from django.db import models
from django.db.models.deletion import CASCADE
from aluno.models import Aluno
from materia.models import Materia

# Create your models here.

class BimestreModel(models.Model):
    ano_letivo = models.CharField(max_length=4)
    bimestre = models.CharField(max_length=50)


class BoletimModel(models.Model):
    aluno_bimestre = models.ForeignKey(Aluno,on_delete=CASCADE)
    bimestre = models.ForeignKey(BimestreModel, on_delete=CASCADE)
    materia = models.ForeignKey(Materia,on_delete=CASCADE)
    data_inclusao = models.DateTimeField("Data de Inclusão",auto_now_add=True)
    nota = models.DecimalField("Nota",max_digits=4, decimal_places=2)