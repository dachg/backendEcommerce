from django.db import models

# Create your models here.
class Departamento(models.Model):
    departamento_id = models.IntegerField()
    code = models.IntegerField()
    name = models.CharField(max_length=200)

class Municipio(models.Model):
    municipio_id = models.IntegerField()
    departamento_id = models.IntegerField()
    code = models.IntegerField()
    name = models.CharField(max_length=200)

class CategoriaProducto(models.Model):
    categoria_producto_id = models.IntegerField()
    categoria_padre_id  = models.IntegerField()
    name = models.CharField(max_length=200)

class Direccion(models.Model):
    direccion_id = models.IntegerField()
    usuario_id = models.IntegerField()
    municipio_id = models.IntegerField()
    direccion = models.CharField(max_length=200)
    direccion_actual = models.BooleanField

