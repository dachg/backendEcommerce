from django.db import models

# Create your models here.
class Departamento(models.Model):
    departamento_id = models.IntegerField()
    code = models.IntegerField()
    name = models.CharField(max_length=200)

class Municipio(models.Model):
    municipio_id = models.IntegerField()
    departamento_id = models.ForeignKey()
    code = models.IntegerField()
    name = models.CharField(max_length=200)

class CategoriaProducto(models.Model):
    categoria_producto_id = models.IntegerField()
    categoria_padre_id  = models.IntegerField()
    name = models.CharField(max_length=200)

class Direccion(models.Model):
    direccion_id = models.IntegerField()
    usuario_id = models.ForeignKey()
    municipio_id = models.ForeignKey()
    direccion = models.CharField(max_length=200)
    direccion_actual = models.BooleanField

class Producto(models.Model):
    producto_id = models.IntegerField()
    categoria_producto_id = models.ForeignKey()
    orden_date = models.DateField()
    nombre = models.CharField(max_length=200)
    precio = models.FloatField()    

class Factura(models.Model):
    factura_id = models.IntegerField()
    usuario_id = models.ForeignKey()
    direcion_id = models.ForeignKey()
    fecha_factura = models.DateField()
    valor_total = models.IntegerField()




