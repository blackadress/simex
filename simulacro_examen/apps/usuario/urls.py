from django.urls import path, re_path

from . import views

app_name = 'usuario'

urlpatterns = [
    # path('/nuevo', views.ViewUsuarioNuevo.as_view(), name='view_usuario_nuevo'),
    # path('/listar', views.ViewUsuarioListar.as_view(), name='view_usuario_listar'),
    # path('/listar/<int:pk>', views.ViewUsuarioUD.as_view(), name='view_usuario_UD'),

    path('alumno-nuevo/', views.ViewAlumnoNuevo.as_view(), name='view_alumno_nuevo'),
    path('alumno-listar/', views.ViewAlumnoListar.as_view(), name='view_alumno_listar'),
    path('alumno-listar/<int:pk>/', views.ViewAlumnoUD.as_view(), name='view_alumno_UD'),

    path('docente-nuevo/', views.ViewDocenteNuevo.as_view(), name='view_docente_nuevo'),
    path('docente-listar/', views.ViewDocenteListar.as_view(), name='view_docente_listar'),
    path('docente-listar/<int:pk>/', views.ViewDocenteUD.as_view(), name='view_docente_UD'),

    path('api/logout/', views.APILogout.as_view(), name='api_logout'),
]
