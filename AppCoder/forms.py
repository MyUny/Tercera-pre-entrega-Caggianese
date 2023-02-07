from django import forms

class CursoFormulario(forms.Form):
    
    curso = forms.CharField()
    camada = forms.IntegerField()
    
class entregablesForm(forms.Form):
    nombre = forms.CharField()
    fechaDeEntrega = forms.DateField()
    entregado = forms.BooleanField(widget=forms.CheckboxInput())
    