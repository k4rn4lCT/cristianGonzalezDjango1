from django.shortcuts import render,redirect
from .forms import UsuarioForm,SerieForm,PlataformaForm,UserEditForm
from .models import Usuario,Serie,Plataforma
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash


# ================================== INDEX =======================================================
@login_required
def index(request):
    return render(request,'SeriesUY/index.html')

# ================================== USUARIO =======================================================
@login_required
def cargar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'SeriesUY/usuario_form.html', {'form':form})

@login_required
def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'SeriesUY/lista_usuarios.html',{'usuarios': usuarios})

# ================================== SERIE =======================================================
@login_required
def cargar_serie(request):
    if request.method == 'POST':
        form = SerieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_series')
    else:
        form = SerieForm()
    return render(request, 'SeriesUY/serie_form.html', {'form':form})

@login_required
def lista_series(request):
    series = Serie.objects.all()
    return render(request, 'SeriesUY/lista_series.html',{'series': series})

# ================================== PLATAFORMA =======================================================
@login_required
def cargar_plataforma(request):
    if request.method == 'POST':
        form = PlataformaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_plataformas')
    else:
        form = PlataformaForm()
    return render(request, 'SeriesUY/plataforma_form.html', {'form':form})

@login_required
def lista_plataformas(request):
    plataformas = Plataforma.objects.all()
    return render(request, 'SeriesUY/lista_plataformas.html',{'plataformas': plataformas})

# ================================== BUSCADOR =======================================================
@login_required
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

# ================================== register =======================================================
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirige al login después de registrar al usuario
        else:
            # Si el formulario no es válido, pasamos el formulario con los errores al template
            return render(request, 'SeriesUY/register.html', {'form': form})
    else:
        form = UserCreationForm()
    return render(request, 'SeriesUY/register.html', {'form': form})


@login_required
def about(request):
    return render(request,'SeriesUY/about.html')

@login_required
def perfil(request):
    usuario = request.user
    return render(request, 'SeriesUY/perfil.html', {'usuario': usuario})

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=request.user)
        password_form = PasswordChangeForm(request.user, request.POST)

        if user_form.is_valid() and password_form.is_valid():
            user_form.save()
            password_form.save()
            update_session_auth_hash(request, password_form.user)
            return redirect('perfil')
    else:
        user_form = UserEditForm(instance=request.user)
        password_form = PasswordChangeForm(request.user)

    return render(request, 'SeriesUY/editar_perfil.html', {
        'user_form': user_form,
        'password_form': password_form,
    })