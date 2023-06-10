from django.shortcuts import render
from django.http import JsonResponse
from .controller import *
# Create your views here.


def home(request):
    return render(request,'core/home.html')

def productos(request):
     variable  = {
          'mensaje':'',
          'lista':''
     }
     controller = Controller()
     try:
          lista = controller.mostrarTodo()
          variable['lista']=lista
          variable['mensaje']="Con datos"
     except:
          variable['mensaje']="sin datos"

     return render(request,'core/productos.html', variable)


##por hacer
def buscarLibro(request):
     controller = Controller()
     codigo = request.POST.get('codigo')
     libro = controller.buscarUnLibro(codigo)
     return JsonResponse({
          'codigo': libro.id_producto,
          'nombre': libro.nombre,
          'tipo': libro.tipo,
          'descripcion':libro.autor,
          'precio': libro.precio,
          'stock': libro.stock,
          'estado':libro.estado

     })

def actualizarLibro(request):
     controller = Controller()
     codigo = request.POST.get('id_producto')
     stock  = request.POST.get('stock')
     resultado = controller.actualizarStock(codigo,stock)
     return JsonResponse({
          'mensaje': resultado
     })