from django.shortcuts import redirect, render
from materia.forms import MateriaForm
from materia.models import Materia

def delete_materia(request,id):
    obj_materia = Materia.objects.get(pk=id)
    obj_materia.delete()
    
    return redirect("list_materia")

def list_materia(request):
    dados =dict()
    
    obj_materias = Materia.objects.all() 
    dados['materias'] = obj_materias
   
    return render(request,'materia/form_list_materia.html', dados)
    
# Create your views here.
def add_materia(request):
    form = MateriaForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect("list_materia")    
    
    dados = dict()
    dados["materiaForm"] = MateriaForm
    return render(request,"materia/form_add_materia.html",dados)

def alter_materia(request, id):
    object_materia = Materia.objects.get(pk=id)
    
    form = MateriaForm(request.POST or None, instance = object_materia)

    if form.is_valid():
        form.save()
        return redirect("list_materia")
    
    dados = dict()
    dados["materiaForm"] = form
    dados["transacao"] = object_materia
    
    return render(request, "materia/form_add_materia.html",dados)