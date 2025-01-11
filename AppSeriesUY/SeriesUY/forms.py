from django import forms
from .models import Usuario,Serie,Plataforma

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields= ['rol','nombreUsuario','correo']
        
class SerieForm(forms.ModelForm):
    class Meta:
        model = Serie
        fields = ['titulo','puntuacion']

class PlataformaForm(forms.ModelForm):
    class Meta:
        model = Plataforma
        fields = ['nombre','precio']