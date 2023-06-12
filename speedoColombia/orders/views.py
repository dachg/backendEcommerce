from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from rest_framework.generics import CreateAPIView,RetrieveUpdateAPIView,UpdateAPIView,ListAPIView,RetrieveUpdateDestroyAPIView,DestroyAPIView, GenericAPIView
from .serializers import ProductoSerializer
from .serializers import CategoriaProductoSerializer
from .serializers import FacturaSerializer
from .models import Producto, CategoriaProducto, Factura

# Create your views here.
class UserListView(ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'object_list'

#@permission_classes((AllowAny, ))
class ProductListApi(ListAPIView):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.filter(precio__gte=200000)


#@permission_classes((AllowAny, ))
class CategoriaProductoListApi(ListAPIView):
    serializer_class = CategoriaProductoSerializer
    queryset = CategoriaProducto.objects.all()

class FacturaCreateApi(CreateAPIView):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

class ProductCreateApi(CreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer