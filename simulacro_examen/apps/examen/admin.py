from django.contrib import admin

from apps.examen.models import Universidad, Facultad, EscuelaProfesional, Examen, ExamenPregunta, Curso, CursoExamen, Pregunta, Alternativa, ResultadoExamen

# Register your models here.

admin.site.register(Alternativa)
admin.site.register(Curso)
admin.site.register(CursoExamen)
admin.site.register(EscuelaProfesional)
admin.site.register(Examen)
admin.site.register(ExamenPregunta)
admin.site.register(Facultad)
admin.site.register(Pregunta)
admin.site.register(ResultadoExamen)
admin.site.register(Universidad)
