from django.shortcuts import render
from django.db import connection
# Create your views here.
import base64

from django.template import base


def aguamineral(request):
    return render(request, 'app/aguamineral.html')

def arroz(request):
    return render(request, 'app/arroz.html')

def bebidas(request):
    return render(request, 'app/bebidas.html')

def busqueda(request):
    return render(request, 'app/busqueda.html')

def cafe(request):
    return render(request, 'app/cafe.html')

def carritodecompras(request):
    return render(request, 'app/carritodecompras.html')

def chocolate(request):
    return render(request, 'app/chocolate.html')

def confort(request):
    return render(request, 'app/confort.html')

def desodoranteamb(request):
    return render(request, 'app/desodoranteamb.html')

def detergente(request):
    return render(request, 'app/detergente.html')

def dulceambroso(request):
    return render(request, 'app/dulceambroso.html')

def fiado(request):
    return render(request, 'app/fiado.html')

def fideos(request):
    return render(request, 'app/fideos.html')

def galleta(request):
    return render(request, 'app/galleta.html')

def home(request):
    return render(request, 'app/home.html')

def huevosdepascua(request):
    return render(request, 'app/huevosdepascua.html')

def InicioSesion(request):
    return render(request, 'app/InicioSesion.html')

def jugos(request):
    return render(request, 'app/jugos.html')

def lavaloza(request):
    return render(request, 'app/lavaloza.html')

def leche(request):
    return render(request, 'app/leche.html')

def maruchan(request):
    return render(request, 'app/maruchan.html')

def mediosdepago(request):
    return render(request, 'app/mediosdepago.html')

def pastadedientes(request):
    return render(request, 'app/pastadedientes.html')

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

    return render(request, 'app/productos.html', data)

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

    return render(request, 'app/catalogo.html', data)

def quienessomos(request):
    return render(request, 'app/quienessomos.html')

def registrarse(request):
    return render(request, 'app/registrarse.html')

def salsatomate(request):
    return render(request, 'app/salsatomate.html')

def te(request):
    return render(request, 'app/te.html')

def yoghurt(request):
    return render(request, 'app/yoghurt.html')

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