from django import forms

from aluno.models import Aluno

class AlunoForm(forms.ModelForm):
    nome = forms.CharField(label="Nome Aluno", max_length=100)
    email = forms.EmailField(label="e-Mail Aluno", max_length=100)
    data_nascimento = forms.DateField(label="Data Nascimento")
    responsavel = forms.CharField(label="Nome Responsável", max_length=100)
    telefone_responsavel = forms.CharField(label="Telefone Responsável", max_length=11)
    
    class Meta():
        model = Aluno
        exclude = ['data_inclusao']