from django.urls import path, re_path

from . import views

app_name = 'examen'

urlpatterns = [
    path('universidad-nuevo/', views.ViewUniversidadNuevo.as_view(), name='view_universidad_nuevo'),
    path('universidad-listar/', views.ViewUniversidadListar.as_view(), name='view_universidad_listar'),
    path('universidad-listar/<int:pk>', views.ViewUniversidadUD.as_view(), name='view_universidad_UD'),

    path('facultad-nuevo/', views.ViewFacultadNuevo.as_view(), name='view_facultad_nuevo'),
    path('facultad-listar/', views.ViewFacultadListar.as_view(), name='view_facultad_listar'),
    path('facultad-listar/<int:pk>', views.ViewFacultadUD.as_view(), name='view_facultad_UD'),

    path('escuela-nuevo/', views.ViewEscuelaNuevo.as_view(), name='view_escuela_nuevo'),
    path('escuela-listar/', views.ViewEscuelaListar.as_view(), name='view_escuela_listar'),
    path('escuela-listar/<int:pk>', views.ViewEscuelaUD.as_view(), name='view_escuela_UD'),

    path('examen-nuevo/', views.ViewExamenNuevo.as_view(), name='view_examen_nuevo'),
    path('examen-listar/', views.ViewExamenListar.as_view(), name='view_examen_listar'),
    path('examen-listar/<int:pk>', views.ViewExamenUD.as_view(), name='view_examen_UD'),

    path('curso-nuevo/', views.ViewCursoNuevo.as_view(), name='view_curso_nuevo'),
    path('curso-listar/', views.ViewCursoListar.as_view(), name='view_curso_listar'),
    path('curso-listar/<int:pk>', views.ViewCursoUD.as_view(), name='view_curso_UD'),

    path('pregunta-nuevo/', views.ViewPreguntaNuevo.as_view(), name='view_pregunta_nuevo'),
    path('pregunta-listar/', views.ViewPreguntaListar.as_view(), name='view_pregunta_listar'),
    path('pregunta-listar/<int:pk>', views.ViewPreguntaUD.as_view(), name='view_pregunta_UD'),

    path('resultado-listar/', views.ViewResultadoListar.as_view(), name='view_resultado_listar'),
    path('resultado-listar/<int:pk>', views.ViewResultadoUD.as_view(), name='view_resultado_UD'),

]
