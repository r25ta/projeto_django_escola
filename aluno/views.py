from django.shortcuts import redirect, render
from aluno.forms import AlunoForm
from aluno.models import Aluno

# Create your views here.
def delete_aluno(request, id):
    obj_aluno = Aluno.objects.get(pk=id)
    obj_aluno.delete()      

    return redirect("list_aluno")

def alter_aluno(request, id):
    dados = dict()
    
    obj_aluno = Aluno.objects.get(pk=id)
    
    form = AlunoForm(request.POST or None, instance = obj_aluno)
    
    if form.is_valid():
        form.save()
        return redirect("list_aluno")
    
    dados["alunoForm"] = form
    dados["transacao"] = obj_aluno
    return render(request, 'aluno/form_aluno.html',dados) 
    

def add_aluno(request):

    form = AlunoForm(request.POST or None)
       
    if form.is_valid():
        form.save()
        return redirect("list_aluno")            
    
    dados = dict()
    dados["alunoForm"] = AlunoForm
    return render(request,'aluno/form_aluno.html',dados)

def list_aluno(request):
    dados = dict()
    obj_alunos = Aluno.objects.all
    
    dados["alunos"] = obj_alunos
    
    return render(request, "aluno/form_list_aluno.html",dados)