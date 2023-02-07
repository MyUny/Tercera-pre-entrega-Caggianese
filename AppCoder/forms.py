from django import forms


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
