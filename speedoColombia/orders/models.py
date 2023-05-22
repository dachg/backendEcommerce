from django.db import models

# Create your models here.
class Departamento(models.Model):
    departamento_id = models.IntegerField(primary_key=True)
    code = models.IntegerField()
    name = models.CharField(max_length=200)

class Municipio(models.Model):
    municipio_id = models.IntegerField(primary_key=True)
    departamento_id = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    code = models.IntegerField()
    name = models.CharField(max_length=200)

class CategoriaProducto(models.Model):
    categoria_producto_id = models.IntegerField(primary_key=True)
    categoria_padre_id  = models.IntegerField()
    name = models.CharField(max_length=200)

class Direccion(models.Model):
    direccion_id = models.IntegerField(primary_key=True)
    usuario_id = models.IntegerField()
    municipio_id = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=200)
    direccion_actual = models.BooleanField(default=False)

class Producto(models.Model):
    producto_id = models.IntegerField(primary_key=True)
    categoria_producto_id = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE)
    orden_date = models.DateField()
    nombre = models.CharField(max_length=200)
    precio = models.FloatField()    

class Factura(models.Model):
    factura_id = models.IntegerField(primary_key=True)
    usuario_id = models.IntegerField()
    direcion_id = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    fecha_factura = models.DateField()
    valor_total = models.IntegerField()

class InventarioProducto(models.Model):
    inventario_producto_id = models.IntegerField(primary_key=True)
    producto_id = models.ForeignKey(Producto, on_delete=models.CASCADE)
    referencia = models.CharField(max_length=200)
    serial = models.CharField(max_length = 200)

class DetalleFactura(models.Model):
    detalle_factura_id = models.IntegerField(primary_key=True)
    factura_id = models.ForeignKey(Factura, on_delete=models.CASCADE)
    inventario_producto_id = models.ForeignKey(InventarioProducto, on_delete=models.CASCADE)
    valor_unitario = models.IntegerField
    unidades_vendidas = models.IntegerField