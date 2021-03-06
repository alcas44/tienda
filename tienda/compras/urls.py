from django import views
from django.urls import path,include
from compras import views


urlpatterns = [
    path('',views.inicio,name="Inicio"),
    path('salir/',views.logout_user,name="Salir"),
    path('compras/',views.compras,name="Compras"),
    path('nuevo/',views.nuevo,name="Nuevo"),
    path('editar/<int:id>',views.editar,name="Editar"),
    path('eliminar/<int:id>',views.eliminar,name="Eliminar"),
    path('error/',views.error,name="Error"),
]
