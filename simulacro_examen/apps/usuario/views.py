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
        context = {}
        return render(request, self.template_name, context)

class ViewAlumnoListar(ListView):
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

    def put(self, request, *args, **kwargs):
        pk = kwargs['pk']
        form = request.PUT
        context = {}
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
        context = {}
        return render(request, self.template_name, context)

class ViewDocenteListar(ListView):
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

    def put(self, request, *args, **kwargs):
        pk = kwargs['pk']
        form = request.PUT
        context = {}
        return render(request, self.template_name, context)

    def delete(self, request, *args, **kwargs):
        pk = kwargs['pk']
        docente = Docente.objects.delete(pk=pk)
        context = {}
        return render(request, self.template_name, context)
