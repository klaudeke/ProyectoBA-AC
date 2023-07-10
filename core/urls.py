from django.urls import path
from django.contrib.auth.views import logout_then_login
from .views  import home,productos,buscarProducto,actualizarStock,bodegaANWO,actualizarStockAnwo,buscarProductoAnwo

urlpatterns = [
    path('', home, name="home"),
    path('productos/',productos, name="productos"),
    path('bodegaANWO/',bodegaANWO, name="bodegaANWO"),
    path('logout', logout_then_login, name="logout"),
    path('post/ajax/buscar',buscarProducto,name="post_buscar"),
    path('post/ajax/actualizar',actualizarStock,name="post_actualizar"),
    path('post/ajax/buscarAnwo',buscarProductoAnwo,name="post_buscar_anwo"),
    path('post/ajax/actualizarAnwo',actualizarStockAnwo,name="post_actualizar_anwo"),
]