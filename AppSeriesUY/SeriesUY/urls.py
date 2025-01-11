from django.urls import path
from .views import index,cargar_usuario,lista_usuarios,cargar_serie,lista_series,cargar_plataforma,lista_plataformas


urlpatterns = [
    path('', index, name='index'),
    path('cargar_usuarios/', cargar_usuario, name = 'cargar_usuario'),
    path('usuarios/',lista_usuarios,name='lista_usuarios'),
    path('cargar_serie/', cargar_serie, name = 'cargar_serie'),
    path('series/',lista_series,name='lista_series'),
    path('cargar_plataforma/', cargar_plataforma, name = 'cargar_plataforma'),
    path('plataformas/',lista_plataformas,name='lista_plataformas'),
]