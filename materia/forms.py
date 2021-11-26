from django import forms
from materia.models import Materia

class MateriaForm(forms.ModelForm):
    nome = forms.CharField(label="Nome da disciplina", max_length=50, required=True)
    sigla = forms.CharField(label="Sigla da disciplina", max_length=3, required=True)
    
    class Meta:
        model = Materia
        exclude = ['data_inclusao']