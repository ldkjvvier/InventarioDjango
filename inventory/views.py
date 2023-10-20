from django.shortcuts import render
from .models import Producto

# Create your views here.


def index(request):
    productos = Producto.objects.all().order_by('nombre')
    data = {
        'productos': productos
    }
    return render(request, 'index.html', data)

