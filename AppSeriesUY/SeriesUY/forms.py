from django import forms
from .models import Usuario,Serie,Plataforma
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm

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
        
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class PasswordChangeForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput)
    new_password1 = forms.CharField(widget=forms.PasswordInput)
    new_password2 = forms.CharField(widget=forms.PasswordInput)
    
