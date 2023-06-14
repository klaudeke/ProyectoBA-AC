from zeep import Client
from .bodega import Pbodega
from django.http import JsonResponse
import mercadopago  

class Controller:
    wsdl= 'http://localhost:8080/WebApplicationBodega/WSBodega?wsdl'
    cliente = Client(wsdl)

    def mostrarTodo(self):
        listaBodega =[]
        lista = self.cliente.service.consultarProductos()
        for i in range(len(lista)):
            #id_producto,nombre,precio,stock,autor,vigencia
            producto = Pbodega(
                            lista[i]['ID_PRODUCTO'],
                            lista[i]['NOMBRE'],
                            lista[i]['TIPO'],
                            lista[i]['DESCRIPCION'],
                            lista[i]['PRECIO'],
                            lista[i]['STOCK'],
                            lista[i]['ESTADO']
                          )
  
            listaBodega.append(producto)
        return listaBodega
    

    def buscarUnProducto(self,cod):
        producto = self.cliente.service.ConsultarUnProducto(cod)
        return producto
    
    
    def actualizarStock(self,cod,stock):
        resultado = self.cliente.service.actualizarStock(cod,stock)
        return resultado
    
    def pagar(self):
        # Agrega credenciales
        sdk = mercadopago.SDK("TEST-6893203693292695-052520-30a71d70f230d155da862fb8159a6138-1381511191")

        #crea preferencia
        preference_data={
            "items":[
                {
                    "title":"Mi AC",
                    "quantity": 1,
                    "unit_price": 289990
                }
            ]
        }

        preference_response = sdk.preference().create(preference_data)
        #preference = preference_response["response"]
        return preference_response
