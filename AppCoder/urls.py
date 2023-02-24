from django.urls import path
from django.contrib.auth.views import LogoutView
from AppCoder import views

urlpatterns = [
    path('inicio', views.inicio, name='inicio'),    
    path('profesor', views.profesor, name="profesor"),      
    path('cursoFormulario', views.cursoFormulario, name="cursoFormulario"),
    path('busquedaCamada', views.busquedaCamada, name="busquedaCamada"),
    path('buscar/', views.buscar),
    path('entregableFormulario', views.entregableFormulario, name="entregableFormulario"),
    path('estudianteFormulario', views.estudianteFormulario, name="estudianteFormulario"),
    path('register', views.register, name = 'Register'),
    path('login/', views.login_request, name = 'Login'),
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name='Logout'),
]



