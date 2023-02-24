from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso, Entregable, Estudiante, Profesor
from django.forms import *
from django.shortcuts import redirect
from AppCoder.forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def inicio(request):
    return render(request, "AppCoder/inicio.html")

def estudianteFormulario(request):
    if request.method == 'POST':

        miFormulario = estudianteForm(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            estudiante = Estudiante(nombre=informacion['nombre'],
                                    apellido=informacion['apellido'], email=informacion['email'])

            estudiante.save()

            return redirect("estudianteFormulario")

    else:

        miFormulario = estudianteForm()
    return render(request, "AppCoder/estudianteFormulario.html", {"miFormulario": miFormulario})


def cursoFormulario(request):
    if request.method == 'POST':

        miFormulario = CursoFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            curso = Curso(curso=informacion['curso'],
                          camada=informacion['camada'])

            curso.save()

            return redirect("cursoFormulario")

    else:

        miFormulario = CursoFormulario()
    return render(request, "AppCoder/cursoFormulario.html", {"miFormulario": miFormulario})


def busquedaCamada(request):

    return render(request, "AppCoder/busquedaCamada.html")


def buscar(request):

   # respuesta = f"Estoy buscando la camada nro: {request.GET['camada']}"
    # return HttpResponse(respuesta)
    if request.GET["camada"]:

        camada = request.GET['camada']
        cursos = Curso.objects.filter(camada__icontains=camada)

        return render(request, "AppCoder/resultadosBusqueda.html", {"cursos": cursos, "camada": camada})

    else:

        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)


def entregableFormulario(request):
    if request.method == 'POST':

        miFormulario = entregablesForm(request.POST)

        print(miFormulario)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            entrega = Entregable(nombre=informacion['nombre'],
                                 fechaDeEntrega=informacion['fechaDeEntrega'], entregado=informacion['entregado'])

            entrega.save()

            return redirect("entregableFormulario")

    else:

        miFormulario = entregablesForm()
    return render(request, "AppCoder/entregableFormulario.html", {"miFormulario": miFormulario})


def profesor(request):
    if request.method == 'POST':

        miFormulario = profesorForm(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            profesor = Profesor(nombre=informacion['nombre'],
                                    apellido=informacion['apellido'], email=informacion['email'], profesion=informacion['profesion'])

            profesor.save()

            return redirect("profesor")

    else:

        miFormulario = profesorForm()
    return render(request, "AppCoder/profesor.html", {"miFormulario": miFormulario})

def register(request):
	
    if request.method == 'POST':
		# Form nativo Django ↓
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
			
            username = form.cleaned_data['username']
            form.save()
            return render(request,"AppCoder/inicio.html" ,  {"mensaje":"Usuario Creado :)"})
    else:
		# Form nativo Django ↓
	    #form = UserCreationForm()       
        form = UserRegisterForm()
    return render(request,"AppCoder/registro.html" ,  {"form":form})