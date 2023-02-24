from django.urls import path
from django.contrib.auth.views import LogoutView
from AppCoder import views

urlpatterns = [
    path('inicio', views.inicio, name='inicio'),    
    path('profesor', views.profesor, name="profesor"),      
    path('cursoFormulario', views.cursoFormulario, name="cursoFormulario"),
    path('comentarioFormulario', views.comentarioFormulario, name="comentarioFormulario"),
    path('busquedaCamada', views.busquedaCamada, name="busquedaCamada"),
    path('buscar/', views.buscar),
    path('entregableFormulario', views.entregableFormulario, name="entregableFormulario"),
    path('estudianteFormulario', views.estudianteFormulario, name="estudianteFormulario"),
    path('register', views.register, name = 'Register'),
    path('login/', views.login_request, name = 'Login'),
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name='Logout'),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    path('curso/list', views.CursoList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.CursoDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.CursoCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.CursoUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.CursoDelete.as_view(), name='Delete'),
]



