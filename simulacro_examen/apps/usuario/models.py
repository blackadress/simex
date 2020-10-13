from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Usuario(models.Model):
    TIPO_USUARIO = (
        ("alumno", "alumno"),
        ("docente", "docente"),
        ("administrador", "administrador"),
    )
    nombres = models.CharField(max_length=200, null=False)
    apellido_paterno = models.CharField(max_length=200, null=False)
    apellido_materno = models.CharField(max_length=200, null=False)
    correo_electronico = models.CharField(max_length=200, null=False)
    celular = models.CharField(max_length=9, null=True, blank=True, default="000000000")
    tipo_usuario = models.CharField(max_length=13, blank=False, null=False, default="alumno", choices=TIPO_USUARIO)

    usuario = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

class Docente(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Docente"
        verbose_name_plural = "Docentes"

class Alumno(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"

