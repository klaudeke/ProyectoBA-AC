from django.urls import path
from .views  import home,productos,buscarProducto,actualizarLibro

urlpatterns = [
    path('', home, name="home"),
    path('productos/',productos, name="productos"),
    path('post/ajax/buscar',buscarProducto,name="post_buscar"),
    path('post/ajax/actualizar',actualizarLibro,name="post_actualizar"),
]