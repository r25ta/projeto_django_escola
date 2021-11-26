from django.shortcuts import render

from boletim.models import BoletimModel

# Create your views here.
def list_boletim(request):
    dados = dict()
    obj_boletim = BoletimModel.objects.all()
    dados["boletins"] = obj_boletim
    
    return render(request,"boletim/form_list_boletim.html",dados)
    