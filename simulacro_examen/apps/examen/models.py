from ckeditor.fields import RichTextField
from django.db import models

from apps.usuario.models import Alumno, Docente

# Create your models here.


class Universidad(models.Model):
    nombre = models.CharField(max_length=200, null=False)
    siglas = models.CharField(max_length=200, null=False)

    class Meta:
        verbose_name = "Universidad"
        verbose_name_plural = "Universidades"

    def __str__(self):
        return "{} {}".format(self.siglas, self.nombre)


class Facultad(models.Model):
    nombre = models.CharField(max_length=200, null=False)

    universidad = models.ForeignKey(
        "Universidad", on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Facultad"
        verbose_name_plural = "Facultades"

    def __str__(self):
        return "{} {}".format(self.universidad.siglas, self.nombre)


class EscuelaProfesional(models.Model):
    nombre = models.CharField(max_length=200, null=False)

    facultad = models.ForeignKey(
        "Facultad", on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Escuela Profesional"
        verbose_name_plural = "Escuelas Profesionales"

    def __str__(self):
        return "{} {}".format(self.facultad.nombre, self.nombre)


class Examen(models.Model):
    nombre_examen = models.CharField(max_length=200, null=False)
    tipo_examen = models.CharField(max_length=200, null=False)
    duracion_minutos = models.IntegerField(default=60)
    nota_maxima = models.DecimalField(max_digits=6, decimal_places=3)
    puntaje_maximo = models.DecimalField(max_digits=6, decimal_places=3)

    universidad = models.ForeignKey(
        "Universidad", on_delete=models.SET_NULL, null=True)
    # examen_pregunta = models.ForeignKey("ExamenPregunta", on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Examen"
        verbose_name_plural = "Examenes"


class ExamenPregunta(models.Model):
    examen = models.ForeignKey("Examen", on_delete=models.SET_NULL, null=True)
    pregunta = models.ForeignKey(
        "Pregunta", on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Examen Pregunta"
        verbose_name_plural = "Examenes Preguntas"


class Curso(models.Model):
    nombre = models.CharField(max_length=200, null=False)
    siglas = models.CharField(max_length=200, null=False)

    universidad = models.ForeignKey(
        "Universidad", on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

    def __str__(self):
        return "{} -- {}".format(self.siglas, self.nombre)


class CursoExamen(models.Model):
    cantidad_preguntas = models.IntegerField()
    favor = models.DecimalField(max_digits=6, decimal_places=3)
    contra = models.DecimalField(max_digits=6, decimal_places=3)
    sin_responder = models.DecimalField(max_digits=6, decimal_places=3)

    curso = models.ForeignKey("Curso", on_delete=models.SET_NULL, null=True)
    examen = models.ForeignKey("Examen", on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Curso de examen"
        verbose_name_plural = "Cursos de examen"


class Pregunta(models.Model):
    nombre = models.CharField(max_length=200, null=False)
    contenido = RichTextField(max_length=300, null=False)

    curso = models.ForeignKey("Curso", on_delete=models.SET_NULL, null=True)
    docente = models.ForeignKey(Docente, on_delete=models.SET_NULL, null=True)
    # examen_pregunta = models.ForeignKey("ExamenPregunta", on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Pregunta"
        verbose_name_plural = "Preguntas"

    def __str__(self):
        return "{}".format(self.nombre)


class Alternativa(models.Model):
    alternativa = RichTextField(max_length=200, null=False)
    clave = models.CharField(max_length=200, null=True)
    correcta = models.BooleanField(default=False)

    pregunta = models.ForeignKey(
        "Pregunta", on_delete=models.SET_NULL, null=True, related_name="alternativas", related_query_name="alternativas")

    class Meta:
        verbose_name = "Alternativa"
        verbose_name_plural = "Alternativas"

    def __str__(self):
        return "{}".format(self.alternativa)


class ResultadoExamen(models.Model):
    duracion_segundos = models.IntegerField()
    nota_obtenida = models.DecimalField(max_digits=7, decimal_places=3)
    puntaje_obtenido = models.DecimalField(max_digits=7, decimal_places=3)

    examen = models.ForeignKey("Examen", on_delete=models.SET_NULL, null=True)
    alumno = models.ForeignKey(Alumno, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Resultado Examen"
        verbose_name_plural = "Resultados Examenes"


class ResultadoExamenPregunta(models.Model):
    valor_pregunta = models.DecimalField(max_digits=7, decimal_places=3)

    resultado_examen = models.ForeignKey(
        "ResultadoExamen", on_delete=models.SET_NULL, null=True)
    pregunta = models.ForeignKey(
        "Pregunta", on_delete=models.SET_NULL, null=True)
    alternativa_res = models.ForeignKey(
        "Alternativa", on_delete=models.SET_NULL, null=True)
