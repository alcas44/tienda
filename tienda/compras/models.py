from tabnanny import verbose
from django.db import models

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200,unique=True)#evita tener el mismo nombre
    categoria = models.CharField(max_length=200)
    cantidad = models.IntegerField()
    precio = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:#nombre que tendran en singular y plural
        verbose_name="producto"
        verbose_name_plural="productos"

    def __str__(self):
        return self.nombre #como va a aparecer en el panel admin