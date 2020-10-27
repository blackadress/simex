from django.contrib import admin
from apps.usuario.models import Alumno, Docente, Usuario

# Register your models here.
admin.site.register(Alumno)
admin.site.register(Docente)
admin.site.register(Usuario)
