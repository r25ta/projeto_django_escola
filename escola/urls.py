"""escola URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from aluno.views import add_aluno, list_aluno, alter_aluno, delete_aluno
from boletim.views import list_boletim
from materia.views import add_materia, alter_materia, delete_materia, list_materia

urlpatterns = [
    path('admin/', admin.site.urls),
    #APP ALUNO
    path('add_aluno/',add_aluno, name="add_aluno"),
    path('alter_aluno/<int:id>/',alter_aluno ,name="alter_aluno"),
    path("delete_aluno/<int:id>/",delete_aluno ,name ="delete_aluno"),
    path('',list_aluno, name="list_aluno"),
    #APP MATERIA
    path('list_materia/',list_materia,name='list_materia'),
    path('add_materia/',add_materia, name='add_materia'),
    path('alter_materia/<int:id>/',alter_materia,name='alter_materia'),
    path('delete_materia/<int:id>/',delete_materia,name='delete_materia'),
    #APP BOLETIM
    path('list_boletim/',list_boletim,name='list_boletim')
]
