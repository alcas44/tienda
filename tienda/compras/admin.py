from django.contrib import admin
from .models import *

class ProductosAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")
    list_display=("nombre","categoria","cantidad","precio")
 










admin.site.register(Producto,ProductosAdmin)