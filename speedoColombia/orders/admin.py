from django.contrib import admin
from .models import Departamento
from .models import Municipio
from .models import CategoriaProducto
from .models import Direccion
from .models import Producto
from .models import Factura
from .models import InventarioProducto
from .models import DetalleFactura

# Register your models here.s
admin.site.register(Departamento)
admin.site.register(Municipio)
admin.site.register(CategoriaProducto)
admin.site.register(Direccion)
admin.site.register(Producto)
admin.site.register(Factura)
admin.site.register(InventarioProducto)
admin.site.register(DetalleFactura)