from django.db import models

from apps.usuario.models import Alumno, Docente

# Create your models here.

class Universidad(models.Model):
    nombre = models.CharField(max_length=200, null=False)

    class Meta:
        verbose_name = "Universidad"
        verbose_name_plural = "Universidades"

class Facultad(models.Model):
    nombre = models.CharField(max_length=200, null=False)

    universidad = models.ForeignKey("Universidad", on_delete=models.SET_NULL, null=True)
    class Meta:
        verbose_name = "Facultad"
        verbose_name_plural = "Facultades"

class EscuelaProfesional(models.Model):
    nombre = models.CharField(max_length=200, null=False)

    facultad = models.ForeignKey("Facultad", on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Escuela Profesional"
        verbose_name_plural = "Escuelas Profesionales"

class Examen(models.Model):
    nombre_examen = models.CharField(max_length=200, null=False)
    tipo_examen = models.CharField(max_length=200, null=False)
    duracion_minutos = models.IntegerField(default=60)
    nota_maxima = models.DecimalField(max_digits=4, decimal_places=3)
    puntaje_maximo = models.DecimalField(max_digits=4, decimal_places=3)

    universidad = models.ForeignKey("Universidad", on_delete=models.SET_NULL, null=True)
    # examen_pregunta = models.ForeignKey("ExamenPregunta", on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Examen"
        verbose_name_plural = "Examenes"

class ExamenPregunta(models.Model):
    examen = models.ForeignKey("Examen", on_delete=models.SET_NULL, null=True)
    pregunta = models.ForeignKey("Pregunta", on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Examen Pregunta"
        verbose_name_plural = "Examenes Preguntas"

class Curso(models.Model):
    nombre = models.CharField(max_length=200, null=False)
    siglas = models.CharField(max_length=200, null=False)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

class CursoExamen(models.Model):
    cantidad_preguntas = models.IntegerField()
    favor = models.DecimalField(max_digits=3, decimal_places=3)
    contra = models.DecimalField(max_digits=3, decimal_places=3)
    sin_responder = models.DecimalField(max_digits=3, decimal_places=3)

    curso = models.ForeignKey("Curso", on_delete=models.SET_NULL, null=True)
    examen = models.ForeignKey("Examen", on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Curso de examen"
        verbose_name_plural = "Cursos de examen"

class Pregunta(models.Model):
    nombre = models.CharField(max_length=200, null=False)
    contenido = models.CharField(max_length=300, null=False)

    curso = models.ForeignKey("Curso", on_delete=models.SET_NULL, null=True)
    docente = models.ForeignKey(Docente, on_delete=models.SET_NULL, null=True)
    # examen_pregunta = models.ForeignKey("ExamenPregunta", on_delete=models.SET_NULL, null=True)
    class Meta:
        verbose_name = "Pregunta"
        verbose_name_plural = "Contenido"

class Alternativa(models.Model):
    alternativa = models.CharField(max_length=200, null=False)
    clave = models.CharField(max_length=200, null=False)

    pregunta = models.ForeignKey("Pregunta", on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Alternativa"
        verbose_name_plural = "Alternativas"

class ResultadoExamen(models.Model):
    duracion_segundos = models.IntegerField()
    nota_obtenida = models.DecimalField(max_digits=4, decimal_places=3)
    puntaje_obtenido = models.DecimalField(max_digits=4, decimal_places=3)

    examen = models.ForeignKey("Examen", on_delete=models.SET_NULL, null=True)
    alumno = models.ForeignKey(Alumno, on_delete=models.SET_NULL, null=True)
    class Meta:
        verbose_name = "Resultado Examen"
        verbose_name_plural = "Resultados Examenes"

