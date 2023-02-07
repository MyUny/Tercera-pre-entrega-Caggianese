from django.urls import path

from AppCoder import views

urlpatterns = [
    path('inicio', views.inicio, name='inicio'),
    path('cursos/', views.cursos, name="cursos"),
    path('profesores', views.profesores, name="profesores"),      
    path('estudiantes', views.estudiantes, name='estudiantes'),
    path('entregables', views.entregables, name='entregables'),
    path('landing', views.landing, name='landing'),
    path('padre', views.padre, name='padre'),
    path('hijo', views.hijo, name='hijo'),
    path('cursoFormulario', views.cursoFormulario, name="cursoFormulario"),
    path('busquedaCamada', views.busquedaCamada, name="busquedaCamada"),
    path('buscar/', views.buscar),
    path('entregableFormulario', views.entregableFormulario, name="entregableFormulario")
]



