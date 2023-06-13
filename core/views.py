from django.shortcuts import render
from django.http import JsonResponse
from .controller import *
# Create your views here.


def home(request):
    return render(request,'core/home.html')

def productos(request):
     variable  = {
          'mensaje':'',
          'lista':'',
          'preference_id':''
     }
     controller = Controller()
     try:
          lista = controller.mostrarTodo()
          variable['lista']=lista
          preferencias = controller.pagar()
          variable['preference_id']=preferencias["response"]["id"]
          #variable['mensaje']="Con datos"
     except:
          variable['mensaje']="sin datos"

     return render(request,'core/productos.html', variable)


##por hacer
def buscarProducto(request):
     controller = Controller()
     codigo = request.POST.get('codigo')
     producto = controller.buscarUnProducto(codigo)
     return JsonResponse({
          'codigo': producto.ID_PRODUCTO,
          'nombre': producto.NOMBRE,
          'tipo': producto.TIPO,
          'descripcion':producto.DESCRIPCION,
          'precio': producto.PRECIO,
          'stock': producto.STOCK,
          'estado':producto.ESTADO
     })

def actualizarLibro(request):
     controller = Controller()
     codigo = request.POST.get('id_producto')
     stock  = request.POST.get('stock')
     resultado = controller.actualizarStock(codigo,stock)
     return JsonResponse({
          'mensaje': resultado
     })