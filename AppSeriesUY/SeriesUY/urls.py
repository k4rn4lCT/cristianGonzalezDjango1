from django.urls import path
from .views import index,buscar,cargar_usuario,lista_usuarios,cargar_serie,lista_series,cargar_plataforma,lista_plataformas,register,about,perfil,editar_perfil
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('', index, name='index'),
    path('cargar_usuarios/', cargar_usuario, name = 'cargar_usuario'),
    path('usuarios/',lista_usuarios,name='lista_usuarios'),
    path('cargar_serie/', cargar_serie, name = 'cargar_serie'),
    path('series/',lista_series,name='lista_series'),
    path('cargar_plataforma/', cargar_plataforma, name = 'cargar_plataforma'),
    path('plataformas/',lista_plataformas,name='lista_plataformas'),
    path('buscar/',buscar,name='buscar'),
    path('login/',LoginView.as_view(template_name='SeriesUY/login.html'),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('register/',register,name='register'),
    path('about/',about,name='about'),
    path('perfil/',perfil,name='perfil'),
    path('editar_perfil/',editar_perfil,name='editar_perfil'),
]