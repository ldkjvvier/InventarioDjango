
from django import forms
from InitialPage.models import Proyecto

class FormProyecto (forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'