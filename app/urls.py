from django.urls import path
from .views import catalogo,delivery,home,vista_prod,busqueda,carritodecompras,fiado,InicioSesion,mediosdepago,productos,quienessomos,registrarse          


urlpatterns = [
    path('', home, name="home"),
    path('vista_prod/<id>/', vista_prod, name="vista_prod"),
    path('busqueda/', busqueda, name="busqueda"),
    path('carritodecompras/', carritodecompras, name="carritodecompras"),
    path('fiado/', fiado, name="fiado"),
    path('InicioSesion/', InicioSesion, name="InicioSesion"),
    path('mediosdepago/', mediosdepago, name="mediosdepago"),
    path('productos/', productos, name="productos"),
    path('quienessomos/', quienessomos, name="quienessomos"),
    path('registrarse/', registrarse, name="registrarse"),
    path('delivery/', delivery, name="delivery"),
    path('catalogo/', catalogo, name="catalogo"),
]
