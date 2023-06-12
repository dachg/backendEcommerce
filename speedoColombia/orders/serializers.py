from .models import Producto,CategoriaProducto, Factura
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import (SerializerMethodField)
from rest_framework import serializers

class CategoriaProductoSerializer(ModelSerializer):
    class Meta:
        model = CategoriaProducto
        fields = '__all__'

class ProductoSerializer(ModelSerializer):
    categoria_producto_id = CategoriaProductoSerializer (many=False)
    class Meta:
        model = Producto
        fields = '__all__'
        #Para mostrar únicamente los campos indicados se debe hacer de la siguiente forma
        #fields = ['field1', 'field2', 'field3']

class FacturaSerializer(ModelSerializer):
    categoriaProducto = CategoriaProductoSerializer(many=False)
    class Meta:
        model = Producto
        fields = '__all__'