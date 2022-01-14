from django.forms import forms
from django.shortcuts import redirect, render
from .models import Producto #importo los modelos para usarlos como plantillas
from .forms import FormProducto #importo el formulario para usar


def compras(request):
    form = Producto.objects.all()
    return render(request,"compras/compras.html",{'form':form})




def nuevo(request):
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




def editar(request,id):
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



def eliminar(request,id):
        try:
            producto = Producto.objects.get(id = id)
            producto.delete()
            return redirect('Compras')#la redireccion es en name del path en la url  path('',views.compras,name="Compras"),
        except:
            return redirect('Error') # path('error/',views.error,name="Error"),
   



def error(request):
    return render(request,'error.html')    