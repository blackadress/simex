from django.urls import path, re_path

from . import views

app_name = 'usuario'

urlpatterns = [
    path('usuario/', views.ViewUsuario.as_view(), name='view_usuario'),
]
