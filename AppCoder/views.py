from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso, Entregable
from django.forms import *
from django.shortcuts import redirect
from AppCoder.forms import CursoFormulario, entregablesForm
# Create your views here.


def inicio(request):
    return render(request, "AppCoder/inicio.html")


def cursos(request):
    return render(request, "AppCoder/cursos.html")


def profesores(request):
    return render(request, "AppCoder/profesores.html")


def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")


def entregables(request):
    return render(request, "AppCoder/entregables.html")


def landing(request):
    return render(request, "AppCoder/landing.html")


def padre(request):
    return render(request, "AppCoder/padre.html")


def hijo(request):
    return render(request, "AppCoder/hijo.html")

# def cursoFormulario(request):
#
#    if request.method == 'POST':
#
#        curso = Curso (request.POST['curso'], request.POST['camada'])
#
#    return render(request, "AppCoder/cursoFormulario.html")

# def cursoFormulario(request):
#    if request.method == 'POST':
#        form = Curso(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect(cursoFormulario)
#    else:
#        form = Curso()
#    return render(request, "AppCoder/cursoFormulario.html", {'form': form})


# def cursoFormulario(request):
    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            curso = Curso(curso=informacion['curso'],
                          camada=informacion['camada'])
            curso.save()
            return render(request, "AppCoder/inicio.html")
        else:
            return render(request, "AppCoder/cursoFormulario.html", {"miFormulario": miFormulario})
    else:
        miFormulario = CursoFormulario()
        return render(request, "AppCoder/cursoFormulario.html", {"miFormulario": miFormulario})


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
