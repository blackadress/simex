from django.urls import path, re_path

from . import views

app_name = 'examen'

urlpatterns = [
    path('curso-nuevo/', views.ViewCursoNuevo.as_view(), name='view_curso_nuevo'),
    path('curso-listar/', views.ViewCursoListar.as_view(),
         name='view_curso_listar'),
    path('curso-listar/<int:pk>/',
         views.ViewCursoUD.as_view(), name='view_curso_UD'),

    path('escuela-nuevo/', views.ViewEscuelaNuevo.as_view(),
         name='view_escuela_nuevo'),
    path('escuela-listar/', views.ViewEscuelaListar.as_view(),
         name='view_escuela_listar'),
    path('escuela-buscar/', views.ViewEscuelaListadoFiltrar.as_view(),
         name='view_escuela_lista_filtrar'),
    path('escuela-buscar/<int:universidad_pk>/<int:facultad_pk>/',
         views.ViewEscuelaFiltrarPages.as_view(), name='view_escuela_lista_pages'),
    path('escuela-listar/<int:pk>/',
         views.ViewEscuelaUD.as_view(), name='view_escuela_UD'),

    path('examen-nuevo/', views.ViewExamenNuevo.as_view(),
         name='view_examen_nuevo'),
    path('examen-nuevo-preguntas/<int:examen_id>/',
         views.ViewExamenNuevoAgregarPreguntas.as_view(), name='view_examen_nuevo_agregar_preguntas'),
    path('examen-listar/', views.ViewExamenListar.as_view(),
         name='view_examen_listar'),
    path('examen-rendir/<int:examen_id>/', views.ViewExamenRendir.as_view(), name='view_examen_rendir'),
    path('examen-buscar/', views.ViewExamenListadoFiltrar.as_view(),
         name='view_examen_lista_filtrar'),
    path('examen-buscar/<int:universidad_pk>/',
         views.ViewExamenFiltrarPages.as_view(), name='view_examen_lista_pages'),
    path('examen-listar/<int:pk>',
         views.ViewExamenUD.as_view(), name='view_examen_UD'),

    path('facultad-nuevo/', views.ViewFacultadNuevo.as_view(),
         name='view_facultad_nuevo'),
    path('facultad-listar/', views.ViewFacultadListar.as_view(),
         name='view_facultad_listar'),
    path('facultad-buscar/', views.ViewFacultadListadoFiltrar.as_view(),
         name='view_facultad_lista_filtrar'),
    path('facultad-buscar/<int:universidad_pk>/',
         views.ViewFacultadFiltrarPages.as_view(), name='view_facultad_lista_pages'),
    path('facultad-listar/<int:pk>/',
         views.ViewFacultadUD.as_view(), name='view_facultad_UD'),

    path('pregunta-nuevo/', views.ViewPreguntaNuevo.as_view(),
         name='view_pregunta_nuevo'),
    path('pregunta-listar/', views.ViewPreguntaListar.as_view(),
         name='view_pregunta_listar'),
    path('pregunta-buscar/', views.ViewPreguntaListadoFiltrar.as_view(),
         name='view_pregunta_lista_filtrar'),
    path('pregunta-buscar/<int:curso_id>/',
         views.ViewPreguntaFiltrarPages.as_view(), name='view_examen_lista_pages'),
    path('pregunta-listar/<int:pk>',
         views.ViewPreguntaUD.as_view(), name='view_pregunta_UD'),

    path('resultado-listar/', views.ViewResultadoListar.as_view(),
         name='view_resultado_listar'),
    path('resultado-buscar/', views.ViewResultadoListadoFiltrar.as_view(),
         name='view_resultado_lista_filtrar'),
    path('resultado-buscar/<int:universidad_id>/',
         views.ViewResultadoFiltrarPages.as_view(), name='view_resultado_filtrar_pages'),
    path('resultado-listar/<int:alumno_pk>/',
         views.ViewResultadoUD.as_view(), name='view_resultado_UD'),

    path('universidad-nuevo/', views.ViewUniversidadNuevo.as_view(),
         name='view_universidad_nuevo'),
    path('universidad-listar/', views.ViewUniversidadListar.as_view(),
         name='view_universidad_listar'),
    path('universidad-listar/<int:pk>/',
         views.ViewUniversidadUD.as_view(), name='view_universidad_UD'),

    # API
    # UPLOAD IMG
    path('api/upload-img/', views.APIUploadImg.as_view(), name='api_upload_img'),
    # CURSO
    path('api/curso-buscar-por-universidad/<int:universidad_pk>/',
         views.APIGetCursosByUniversidadId.as_view(), name='api_get_cursos_by_universidad_id'),

    # CURSO_EXAMEN
    path('api/curso-examen-nuevo/<int:examen_id>/',
         views.APICursoExamenNuevo.as_view(), name='api_curso_examen_nuevo'),

    # EXAMEN_PREGUNTA
    path('api/examen-pregunta/nuevo/', views.APIExamenPreguntaNuevo.as_view(),
         name='api_examen_pregunta_nuevo'),
    path('api/examen-pregunta/<int:ex_preg_id>/',
         views.APIExamenPreguntaDetails.as_view(), name='api_curso_examen_detalles'),

    # FACULTAD
    path('api/facultad-buscar/<int:universidad_id>/',
         views.APIGetFacultadesByUniversidadId.as_view(), name='api_get_facultades_by_universidad'),

    # PREGUNTAS
    path('api/pregunta-buscar/<int:docente_pk>/<int:curso_pk>/<str:nombre_pregunta>/<int:examen_id>/',
         views.APIGetPreguntasByDocenteCursoPregunta.as_view(), name='api_get_preguntas_by_docente_curso_pregunta')


]
