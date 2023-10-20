from django.shortcuts import render
from . import forms

# Create your views here.

def index(request):
    return render(request, 'index.html')



def lista_proyectos(request):
    form = forms.UserRegistrationForm()
    data = {'form' : form}
    return render(request, "proyectos.html", data)