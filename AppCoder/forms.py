from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CursoFormulario(forms.Form):

    curso = forms.CharField()
    camada = forms.IntegerField()


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