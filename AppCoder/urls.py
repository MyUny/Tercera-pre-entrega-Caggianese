from django.urls import path
from django.contrib.auth.views import LogoutView
from AppCoder import views

urlpatterns = [
    path('inicio', views.inicio, name='inicio'),        
    path('cursoFormulario', views.cursoFormulario, name="cursoFormulario"),
    path('comentario/comentarioFormulario', views.comentarioFormulario, name="comentarioFormulario"),
    path('busquedaCamada', views.busquedaCamada, name="busquedaCamada"),
    path('buscar/', views.buscar),   
    path('register', views.register, name = 'Register'),
    path('login/', views.login_request, name = 'Login'),
    path('posts/poo', views.programacionOO, name = 'POO'),
    path('e404', views.e404, name = 'e404'),
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name='Logout'),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    path('comentario/list', views.ComentarioList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.ComentarioDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.ComentarioCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.ComentarioUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.ComentarioDelete.as_view(), name='Delete'),
    path('agregarAvatar', views.agregarAvatar, name="AgregarAvatar"),
]



