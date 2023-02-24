from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso, Entregable, Estudiante, Profesor, Avatar, Comentario
from django.forms import *
from django.shortcuts import redirect
from AppCoder.forms import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.

@login_required(login_url='/AppCoder/login/')
def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, "AppCoder/inicio.html", {"url":avatares[0].imagen.url})

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

def comentarioFormulario(request):
    if request.method == 'POST':

        miFormulario = ComentarioFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            comentario = Comentario(comentario=informacion['comentario'],
                          firma=informacion['firma'])

            comentario.save()

            return redirect("comentarioFormulario")

    else:

        miFormulario = ComentarioFormulario()
    return render(request, "AppCoder/comentarioFormulario.html", {"miFormulario": miFormulario})


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

@csrf_protect
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('inicio')  # redirigir al usuario a la página de inicio
            else:
                mensaje = 'Datos incorrectos'
        else:
            mensaje = 'Formulario incorrecto'
    else:
        form = AuthenticationForm()
        mensaje = ''
    return render(request, 'AppCoder/login.html', {'form': form, 'mensaje': mensaje})

def logout_request(request):
    logout(request)
    messages.info(request, "Saliste sin problemas")
    return redirect("inicio")

@login_required(login_url='/AppCoder/login/')
def editarPerfil(request):
	
    usuario = request.user
	
    if request.method == 'POST':
		
        miFormulario = UserEditForm(request.POST)
		
        if miFormulario.is_valid():
			
            informacion = miFormulario.cleaned_data
			
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']
            usuario.set_password(informacion['password1'])
            usuario.save()
			
            return render(request, "AppCoder/inicio.html")
		
    else:
		
        miFormulario = UserEditForm(initial={'email': usuario.email})
		
    return render(request, "AppCoder/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})