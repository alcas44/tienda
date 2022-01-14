from dataclasses import field
import imp
from django import forms
from .models import Producto

class FormProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'#significa todos los campos
        #fields = ('nombre','etc',) debe terminar en coma por que es tupla


class LoginForm(forms.ModelForm):
    username = forms.CharField(label="Username", required=True, max_length=30,
                           widget=forms.TextInput(attrs={
                               'class': 'form-control',
                               'name': 'username'}))
    password = forms.CharField(label="Password", required=True, max_length=30,
                           widget=forms.PasswordInput(attrs={
                               'class': 'form-control',
                               'name': 'password'}))

