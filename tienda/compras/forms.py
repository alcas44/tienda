from dataclasses import field
import imp
from django import forms
from .models import Producto

class FormProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'#significa todos los campos
        #fields = ('nombre','etc',) debe terminar en coma por que es tupla
