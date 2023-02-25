from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso, Avatar, Comentario
from django.forms import *
from django.shortcuts import redirect
from AppCoder.forms import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
# Create your views here.

@login_required(login_url='/AppCoder/login/')
def inicio(request):
    avatares = Avatar.objects.filter(user=request.user)
    if avatares.exists():
        return render(request, "AppCoder/inicio.html", {"url":avatares[0].imagen.url, "avatares":avatares})
    else:
        return render(request, "AppCoder/inicio.html", {"avatares":avatares})


def cursoFormulario(request):
    if request.method == 'POST':

        miFormulario = CursoFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            curso = Curso(curso=informacion['idea'],
                          camada=informacion['fecha'])

            curso.save()

            return redirect("cursoFormulario")

    else:

        miFormulario = CursoFormulario()
    return render(request, "AppCoder/cursoFormulario.html", {"miFormulario": miFormulario})

@login_required(login_url='/AppCoder/login/')
def comentarioFormulario(request):
    if request.method == 'POST':

        miFormulario = ComentarioFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            comentario = Comentario(comentario=informacion['comentario'],
                          firma=informacion['firma'])

            comentario.save()

            return redirect("List")

    else:

        miFormulario = ComentarioFormulario()
    return render(request, "AppCoder/comentarioFormulario.html", {"miFormulario": miFormulario})

def busquedaCamada(request):

    return render(request, "AppCoder/busquedaCamada.html")

def programacionOO(request):

    return render(request, "AppCoder/ProgramacionOrientadaObjetos.html")

def e404(request):

    return render(request, "AppCoder/error404.html")


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



def register(request):
	
    if request.method == 'POST':
		# Form nativo Django ↓
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
			
            username = form.cleaned_data['username']
            form.save()
            return redirect('inicio')
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

@login_required(login_url='/AppCoder/login/')
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

# Vistas CRUD


class ComentarioList(ListView):
	
	model = Comentario
	template_name = "AppCoder/comentarios_list.html"

class ComentarioDetalle(DetailView):
	
	model = Comentario
	template_name = "AppCoder/comentarios_detalle.html"        

class ComentarioCreacion(CreateView):
	
	model = Comentario
	success_url = "/AppCoder/comentario/list"
	fields = ['comentario','firma']

class ComentarioUpdate(UpdateView):
	
	model = Comentario
	success_url = "/AppCoder/comentario/list"
	fields = ['comentario','firma']
        
class ComentarioDelete(DeleteView):
	
	model = Comentario
	success_url = "/AppCoder/comentario/list"

@login_required(login_url='/AppCoder/login/')
def agregarAvatar(request):
      if request.method == 'POST':

            miFormulario = AvatarFormulario(request.POST, request.FILES) #aquí mellega toda la información del html

            if miFormulario.is_valid():   #Si pasó la validación de Django


                  u = User.objects.get(username=request.user)
                
                  avatar = Avatar (user=u, imagen=miFormulario.cleaned_data['imagen']) 
      
                  avatar.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= AvatarFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/agregarAvatar.html", {"miFormulario":miFormulario})