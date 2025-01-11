from django.shortcuts import render,redirect
from .forms import UsuarioForm,SerieForm,PlataformaForm
from .models import Usuario,Serie,Plataforma

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

