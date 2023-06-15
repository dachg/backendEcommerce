from .models import Producto,CategoriaProducto, Factura, Imagen_banner
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import (SerializerMethodField)
from rest_framework import serializers

class CategoriaProductoSerializer(ModelSerializer):
    class Meta:
        model = CategoriaProducto
        fields = ['name'] #'__all__'

class ProductoSerializer(ModelSerializer):
    categoria_producto_id = CategoriaProductoSerializer (many=False)
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'descripcion_larga', 'imagen', 'categoria_producto_id', 'producto_id'] #'__all__'
        #Para mostrar únicamente los campos indicados se debe hacer de la siguiente forma
        #fields = ['field1', 'field2', 'field3']

class FacturaSerializer(ModelSerializer):
    categoriaProducto = CategoriaProductoSerializer(many=False)
    class Meta:
        model = Producto
        fields = '__all__'

class BannerImages(ModelSerializer):
    class Meta:
        model = Imagen_banner
        fields = ['imagen']
