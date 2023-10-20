from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('proyectos' ,views.lista_proyectos, name="proyectos")
]
