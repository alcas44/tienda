import re
#from telnetlib import AUTHENTICATION
from django.contrib import messages
from django.forms import forms
from django.shortcuts import redirect, render
from .models import Producto #importo los modelos para usarlos como plantillas
from .forms import FormProducto #importo el formulario para usar
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin


def inicio(request):
     if request.method == "POST":
         u = request.POST["user"]
         p = request.POST["pass"]
         ver = authenticate(request,username = u, password = p)
         if u is not None:
             login(request, ver)
             return redirect('Compras')
             
         else:
            return redirect('/')
 
     return render(request, 'compras/index.html')         
    

def logout_user(request):
    logout(request)
    messages.success(request,("Haz Finalizado Sesion "))
    return redirect('/')



def compras(request):
    if request.user.is_authenticated:
        form = Producto.objects.all()
        return render(request,"compras/compras.html",{'form':form})
    else:
        return redirect('/')    


def nuevo(request):
    if request.user.is_authenticated:
        form = FormProducto()
        if request.method == "POST":
            form = FormProducto(request.POST)
     
            if form.is_valid():
              try:
                data = Producto()#tabla a guarda los datos
                data.nombre = form.cleaned_data['nombre']
                data.categoria = form.cleaned_data['categoria']
                data.cantidad = form.cleaned_data['cantidad']
                data.precio = form.cleaned_data['precio']
                data.save()
                return redirect('Nuevo')
              except:
                return redirect('compras/error.html')
        return render(request,"compras/nuevo.html",{'form':form})
    else:
        return redirect('/')


def editar(request,id):
    if request.user.is_authenticated:
        producto = Producto.objects.get(id = id)
        if request.method == 'GET':
            form = FormProducto(instance=producto)
        else:
            form = FormProducto(request.POST,instance = producto)
     
            if form.is_valid():
                try:
                    form.save()
                    return redirect('Compras')#la redireccion es en name del path en la url  path('',views.compras,name="Compras"),
                except:
                    return redirect('Error') # path('error/',views.error,name="Error"),

        return render(request,"compras/editar.html",{'form':form})
    else:
        return redirect('/')    



def eliminar(request,id):
    if request.user.is_authenticated:
        try:
            producto = Producto.objects.get(id = id)
            producto.delete()
            return redirect('Compras')#la redireccion es en name del path en la url  path('',views.compras,name="Compras"),
        except:
            return redirect('Error') # path('error/',views.error,name="Error"),
    else:
        return redirect('/')



def error(request):
    return render(request,'compras/error.html')    