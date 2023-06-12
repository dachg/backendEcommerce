from django.urls import path, re_path
from orders.views import UserListView
from .views import ProductListApi, CategoriaProductoListApi, FacturaCreateApi, ProductCreateApi

urlpatterns = [
    path("listView/", UserListView.as_view(), name="listView"),
    re_path(r"^getproducts$", ProductListApi.as_view(), name="getproducts"),
    re_path(r"^getcategories$", CategoriaProductoListApi.as_view(), name="getcategories"),
    re_path(r"^createFactura$", FacturaCreateApi.as_view(), name="createfactura"),
    re_path(r"^createproduct$", ProductCreateApi.as_view(), name="createproduct"),
]