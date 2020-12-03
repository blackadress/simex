from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from apps.usuario.models import Alumno, Docente, Usuario

# Create your views here.

# VISTAS


class ViewAlumnoNuevo(View):
    template_name = 'alumno/nuevo.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = request.POST
        nombres = form['nombres']
        apellido_paterno = form['apPaterno']
        apellido_materno = form['apMaterno']
        email = form['email']
        celular = form['celular']
        usuario = form['usuario']
        password = form['password']
        user = User.objects.create_user(
            username=usuario, email=email, password=password)
        usuario = Usuario.objects.create(
            nombres=nombres,
            apellido_paterno=apellido_paterno,
            apellido_materno=apellido_materno,
            correo_electronico=email,
            celular=celular,
            tipo_usuario="alumno",
            usuario=user
        )
        alumno = Alumno.objects.create(
            usuario=usuario
        )
        msg = "Datos de alumno guardados exitosamente"

        context = {
            "msg": msg
        }
        return render(request, self.template_name, context)


class ViewAlumnoListar(ListView):
    template_name = 'alumno/listar.html'
    paginate_by = 10
    model = Alumno


class ViewAlumnoUD(View):
    template_name = 'alumno/detalles.html'

    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        alumno = Alumno.objects.get(pk=pk)
        context = {
            'alumno': alumno
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        pk = kwargs['pk']
        form = request.POST

        nombres = form['nombres']
        apellido_paterno = form['apPaterno']
        apellido_materno = form['apMaterno']
        email = form['email']
        celular = form['celular']

        alumno = Usuario.objects.filter(pk=pk)
        usuario = alumno[0].usuario
        alumno.update(
            nombres=nombres, apellido_paterno=apellido_paterno,
            apellido_materno=apellido_materno, correo_electronico=email, celular=celular)
        usuario.email = email
        usuario.save(update_fields=["email"])

        context = {
            "alumno": alumno[0]
        }
        return render(request, self.template_name, context)

    def delete(self, request, *args, **kwargs):
        pk = kwargs['pk']
        alumno = Alumno.objects.delete(pk=pk)
        context = {}
        return render(request, self.template_name, context)


class ViewDocenteNuevo(View):
    template_name = 'docente/nuevo.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = request.POST
        nombres = form['nombres']
        apellido_paterno = form['apPaterno']
        apellido_materno = form['apMaterno']
        email = form['email']
        celular = form['celular']
        usuario = form['usuario']
        password = form['password']
        user = User.objects.create_user(
            username=usuario, email=email, password=password)
        usuario = Usuario.objects.create(
            nombres=nombres,
            apellido_paterno=apellido_paterno,
            apellido_materno=apellido_materno,
            correo_electronico=email,
            celular=celular,
            tipo_usuario="docente",
            usuario=user
        )
        docente = Docente.objects.create(
            usuario=usuario
        )
        msg = "Datos de docente guardados exitosamente"

        context = {
            "msg": msg
        }
        return render(request, self.template_name, context)


class ViewDocenteListar(ListView):
    template_name = 'docente/listar.html'
    paginate_by = 10
    model = Docente


class ViewDocenteUD(View):
    template_name = 'docente/detalles.html'

    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        docente = Docente.objects.get(pk=pk)
        context = {
            'docente': docente
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        pk = kwargs['pk']
        form = request.POST

        nombres = form['nombres']
        apellido_paterno = form['apPaterno']
        apellido_materno = form['apMaterno']
        email = form['email']
        celular = form['celular']

        docente = Usuario.objects.filter(pk=pk)
        usuario = docente[0].usuario

        docente.update(
            nombres=nombres, apellido_paterno=apellido_paterno, apellido_materno=apellido_materno,
            correo_electronico=email, celular=celular, tipo_usuario="docente")
        usuario.email = email
        usuario.save(update_fields=["email"])

        context = {
            "docente": docente[0]
        }
        return render(request, self.template_name, context)

    def delete(self, request, *args, **kwargs):
        pk = kwargs['pk']
        docente = Docente.objects.delete(pk=pk)
        context = {}
        return render(request, self.template_name, context)

from django.template.defaulttags import register

@register.filter
def get_tipo_usuario_from_user(user):
    usuario = Usuario.objects.get(usuario=user)
    tipo_usuario = usuario.tipo_usuario
    return tipo_usuario
