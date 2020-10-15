from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from apps.examen.models import Universidad, Facultad, EscuelaProfesional, Examen, ExamenPregunta, Curso, CursoExamen, Pregunta, Alternativa, ResultadoExamen

# Create your views here.
class ViewUniversidadNuevo(View):
    template_name = 'universidad/nuevo.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = request.POST
        context = {}
        return render(request, self.template_name, context)

class ViewUniversidadListar(ListView):
    paginate_by = 10
    model = Universidad

class ViewUniversidadUD(View):
    template_name = 'universidad/detalles.html'

    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        universidad = Universidad.objects.get(pk=pk)
        context = {
            'universidad': universidad
        }
        return render(request, self.template_name, context)

    def put(self, request, *args, **kwargs):
        pk = kwargs['pk']
        form = request.PUT
        context = {}
        return render(request, self.template_name, context)

    def delete(self, request, *args, **kwargs):
        pk = kwargs['pk']
        universidad = Universidad.objects.delete(pk=pk)
        context = {}
        return render(request, self.template_name, context)

class ViewFacultadNuevo(View):
    template_name = 'facultad/nuevo.html'

    def get(self, request, *args, **kwargs):
        universidades = Universidad.objects.all()
        context = {
            "universidades": universidades
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = request.POST
        context = {}
        return render(request, self.template_name, context)

class ViewFacultadListar(ListView):
    paginate_by = 10
    model = Facultad

class ViewFacultadUD(View):
    template_name = 'facultad/detalles.html'

    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        facultad = Facultad.objects.get(pk=pk)
        context = {
            'facultad': facultad
        }
        return render(request, self.template_name, context)

    def put(self, request, *args, **kwargs):
        pk = kwargs['pk']
        form = request.PUT
        context = {}
        return render(request, self.template_name, context)

    def delete(self, request, *args, **kwargs):
        pk = kwargs['pk']
        facultad = Facultad.objects.delete(pk=pk)
        context = {}
        return render(request, self.template_name, context)

class ViewEscuelaNuevo(View):
    template_name = 'escuela/nuevo.html'

    def get(self, request, *args, **kwargs):
        facultades = Facultad.objects.all()
        facultades_formated = []
        for facultad in facultades:
            aux = {
                'id': facultad.id,
                'nombre': facultad.nombre,
                'universidad': facultad.universidad.nombre,
            }
            facultades_formated.append(aux)

        context = {
            "facultades": facultades_formated
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = request.POST
        context = {}
        return render(request, self.template_name, context)

class ViewEscuelaListar(ListView):
    paginate_by = 10
    model = EscuelaProfesional

class ViewEscuelaUD(View):
    template_name = 'escuela/detalles.html'

    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        escuela = EscuelaProfesional.objects.get(pk=pk)
        context = {
            'escuela': escuela
        }
        return render(request, self.template_name, context)

    def put(self, request, *args, **kwargs):
        pk = kwargs['pk']
        form = request.PUT
        context = {}
        return render(request, self.template_name, context)

    def delete(self, request, *args, **kwargs):
        pk = kwargs['pk']
        escuela = EscuelaProfesional.objects.delete(pk=pk)
        context = {}
        return render(request, self.template_name, context)

class ViewExamenNuevo(View):
    template_name = 'examen/nuevo.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = request.POST
        context = {}
        return render(request, self.template_name, context)

class ViewExamenListar(ListView):
    paginate_by = 10
    model = Examen

class ViewExamenUD(View):
    template_name = 'examen/detalles.html'

    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        examen = Examen.objects.get(pk=pk)
        context = {
            'examen': examen
        }
        return render(request, self.template_name, context)

    def put(self, request, *args, **kwargs):
        pk = kwargs['pk']
        form = request.PUT
        context = {}
        return render(request, self.template_name, context)

    def delete(self, request, *args, **kwargs):
        pk = kwargs['pk']
        examen = Examen.objects.delete(pk=pk)
        context = {}
        return render(request, self.template_name, context)

class ViewCursoNuevo(View):
    template_name = 'curso/nuevo.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = request.POST
        context = {}
        return render(request, self.template_name, context)

class ViewCursoListar(ListView):
    paginate_by = 10
    model = Curso

class ViewCursoUD(View):
    template_name = 'curso/detalles.html'

    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        curso = Curso.objects.get(pk=pk)
        context = {
            'curso': curso
        }
        return render(request, self.template_name, context)

    def put(self, request, *args, **kwargs):
        pk = kwargs['pk']
        form = request.PUT
        context = {}
        return render(request, self.template_name, context)

    def delete(self, request, *args, **kwargs):
        pk = kwargs['pk']
        curso = Curso.objects.delete(pk=pk)
        context = {}
        return render(request, self.template_name, context)

class ViewPreguntaNuevo(View):
    template_name = 'pregunta/nuevo.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = request.POST
        context = {}
        return render(request, self.template_name, context)

class ViewPreguntaListar(ListView):
    paginate_by = 10
    model = Pregunta

class ViewPreguntaUD(View):
    template_name = 'pregunta/detalles.html'

    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        pregunta = Pregunta.objects.get(pk=pk)
        context = {
            'pregunta': pregunta
        }
        return render(request, self.template_name, context)

    def put(self, request, *args, **kwargs):
        pk = kwargs['pk']
        form = request.PUT
        context = {}
        return render(request, self.template_name, context)

    def delete(self, request, *args, **kwargs):
        pk = kwargs['pk']
        pregunta = Pregunta.objects.delete(pk=pk)
        context = {}
        return render(request, self.template_name, context)

class ViewResultadoNuevo(View):
    template_name = 'resultado/nuevo.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = request.POST
        context = {}
        return render(request, self.template_name, context)

class ViewResultadoListar(ListView):
    paginate_by = 10
    model = ResultadoExamen

class ViewResultadoUD(View):
    template_name = 'resultado/detalles.html'

    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        resultado = ResultadoExamen.objects.get(pk=pk)
        context = {
            'resultado': resultado
        }
        return render(request, self.template_name, context)

    def put(self, request, *args, **kwargs):
        pk = kwargs['pk']
        form = request.PUT
        context = {}
        return render(request, self.template_name, context)

    def delete(self, request, *args, **kwargs):
        pk = kwargs['pk']
        resultado = ResultadoExamen.objects.delete(pk=pk)
        context = {}
        return render(request, self.template_name, context)

