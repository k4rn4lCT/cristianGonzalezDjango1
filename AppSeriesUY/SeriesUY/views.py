from django.shortcuts import render,redirect
from .forms import UsuarioForm,SerieForm,PlataformaForm
from .models import Usuario,Serie,Plataforma
from django.db.models import Q

# ================================== INDEX =======================================================
def index(request):
    return render(request,'SeriesUY/index.html')

# ================================== USUARIO =======================================================
def cargar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'SeriesUY/usuario_form.html', {'form':form})

def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'SeriesUY/lista_usuarios.html',{'usuarios': usuarios})

# ================================== SERIE =======================================================

def cargar_serie(request):
    if request.method == 'POST':
        form = SerieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_series')
    else:
        form = SerieForm()
    return render(request, 'SeriesUY/serie_form.html', {'form':form})

def lista_series(request):
    series = Serie.objects.all()
    return render(request, 'SeriesUY/lista_series.html',{'series': series})

# ================================== PLATAFORMA =======================================================

def cargar_plataforma(request):
    if request.method == 'POST':
        form = PlataformaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_plataformas')
    else:
        form = PlataformaForm()
    return render(request, 'SeriesUY/plataforma_form.html', {'form':form})

def lista_plataformas(request):
    plataformas = Plataforma.objects.all()
    return render(request, 'SeriesUY/lista_plataformas.html',{'plataformas': plataformas})

# ================================== BUSCADOR =======================================================
def buscar(request):
    query = request.GET.get('q', '')
    resultados = []
    if query:
        usuarios = Usuario.objects.filter(
            Q(rol__icontains=query) | Q(nombreUsuario__icontains=query) | Q(correo__icontains=query)
        )
        series = Serie.objects.filter(
            Q(titulo__icontains=query) | Q(puntuacion__icontains=query)
        )
        plataformas = Plataforma.objects.filter(
            Q(nombre__icontains=query) | Q(precio__icontains=query)
        )

        # Añadir los resultados a la lista
        for usuario in usuarios:
            resultados.append({
                'tipo': 'Usuario',
                'rol': usuario.rol,
                'nombreUsuario': usuario.nombreUsuario,
                'correo': usuario.correo,
            })
        for serie in series:
            resultados.append({
                'tipo': 'Serie',
                'titulo': serie.titulo,
                'puntuacion': serie.puntuacion,
            })
        for plataforma in plataformas:
            resultados.append({
                'tipo': 'Plataforma',
                'nombre': plataforma.nombre,
                'precio': plataforma.precio,
            })

    return render(request, 'SeriesUY/buscar.html', {'resultados': resultados, 'query': query})

            