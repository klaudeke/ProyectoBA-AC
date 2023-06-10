from django.urls import path
from .views  import home,productos,buscarLibro,actualizarLibro

urlpatterns = [
    path('', home, name="home"),
    path('productos/',productos, name="productos"),
    path('post/ajax/buscar',buscarLibro,name="post_buscar"),
    path('post/ajax/actualizar',actualizarLibro,name="post_actualizar"),
]