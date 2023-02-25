from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CursoFormulario(forms.Form):

    idea = forms.CharField()
    fecha = forms.IntegerField()

class ComentarioFormulario(forms.Form):

    comentario = forms.CharField()
    firma = forms.CharField()    


class estudianteForm(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()


class entregablesForm(forms.Form):
    nombre = forms.CharField()
    fechaDeEntrega = forms.DateField()
    entregado = forms.BooleanField(widget=forms.CheckboxInput())


class profesorForm(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    profesion = forms.CharField()

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
	password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
	
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
		# Saca los mensajes de ayuda
		help_texts = {k:"" for k in fields}
                
class UserEditForm(UserCreationForm):

    #Acá se definen las opciones que queres modificar del usuario, 
    #Ponemos las básicas
    email = forms.EmailField(label="Modificar E-mail")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 
    # Mod
    last_name = forms.CharField()
    first_name = forms.CharField()
	
    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2', 'last_name', 'first_name'] 
        #Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}         

class AvatarFormulario(forms.Form):
	
    #Especificar los campos
    
    imagen = forms.ImageField(required=True)                 