from django.shortcuts import render
from django.db import connection
from .models import *
# Create your views here.
import base64

from django.template import base


def vista_prod(request,id):
    id_tipo = TipoProducto.objects.get(id_tipo_producto=id)
    productos = Producto.objects.filter(id_tipo_producto=id_tipo)
    contexto = {"productos":productos}
    return render(request, 'app/vista_prod.html',contexto)

def busqueda(request):
    return render(request, 'app/busqueda.html')

def carritodecompras(request):
    return render(request, 'app/carritodecompras.html')

def fiado(request):
    return render(request, 'app/fiado.html')

def home(request):
    return render(request, 'app/home.html')

def InicioSesion(request):
    return render(request, 'app/InicioSesion.html')

def mediosdepago(request):
    return render(request, 'app/mediosdepago.html')

def catalogo (request):

    datos_tipos = listado_Tipo_Productos()

    arreglo = []

    for i in datos_tipos:
        data = {
            'data':i,
            'img_tipo':str(base64.b64encode(i[2].read()), 'utf-8')
        }
        arreglo.append(data)
    data = {
        'productos': listado_Productos(),
        'categorias': arreglo,
    }

    return render(request, 'app/catalogo.html', data)

def productos(request):

    datos_tipos = listado_Productos()

    arreglo = []

    for i in datos_tipos:
        data = {
            'data':i,
            'img_producto':str(base64.b64encode(i[10].read()), 'utf-8')
        }
        arreglo.append(data)
    data = {
        'productos': listado_Productos(),
        'productos': arreglo,
    }

    return render(request, 'app/productos.html', data)

def quienessomos(request):
    return render(request, 'app/quienessomos.html')

def registrarse(request):
    return render(request, 'app/registrarse.html')

def delivery(request):
    return render(request, 'app/delivery.html')

def listado_Productos():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_PRODUCTOS", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista

def listado_Tipo_Productos():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_TIPO_PRODUCTOS", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista

