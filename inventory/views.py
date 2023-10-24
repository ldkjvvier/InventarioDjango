from django.shortcuts import render
from .forms import FormProyecto
from InitialPage.models import Proyecto

# Create your views here.

def index(request):
    return render(request, 'index.html')



def lista_proyectos(request):
    proyectos = Proyecto.objects.all()
    data = {'proyectos': proyectos}
    return render(request, "proyectos.html", data)

def agregar_proyectos(request):
    form = FormProyecto()
    if request.method == 'POST' :
        form = FormProyecto(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, "agregar_proyectos.html", data)