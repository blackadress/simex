from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from simulacro_examen.settings import OBJ_PER_PAGE

from apps.examen.models import Universidad, Facultad, EscuelaProfesional, Examen, ExamenPregunta, Curso, CursoExamen, Pregunta, Alternativa, ResultadoExamen

# Create your views here.
class ViewUniversidadNuevo(View):
    template_name = 'universidad/nuevo.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = request.POST
        nombre = form['nombre']
        siglas = form['siglas']
        Universidad.objects.create(
            nombre=nombre,
            siglas=siglas,
        )
        msg = "Datos de universidad guardados correctamente"

        context = {
            "msg": msg
        }

        return render(request, self.template_name, context)

class ViewUniversidadListar(ListView):
    template_name = 'universidad/listar.html'
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
        nombre = form['nombre']
        universidad_id = form['universidad']
        Facultad.objects.create(nombre=nombre, universidad_id=universidad_id)
        universidades = Universidad.objects.all()

        msg = "Datos de facultad guardados correctamente"
        context = {
            "msg": msg,
            "universidades": universidades
        }
        return render(request, self.template_name, context)

class ViewFacultadListar(ListView):
    template_name = 'facultad/listar.html'
    paginate_by = 10
    model = Facultad

class ViewFacultadListadoFiltrar(View):
    template_name = 'facultad/lista_filtrar.html'

    def get(self, request, *args, **kwargs):
        universidades = Universidad.objects.all()
        context = {
            "universidades": universidades
        }
        return render(request, self.template_name, context)

class ViewFacultadFiltrarPages(View):
    template_name = 'facultad/lista_filtrar.html'

    def get(self, request, *args, **kwargs):
        page = request.GET['page']
        universidad_id = kwargs['universidad_pk']
        facultades = Facultad.objects.filter(universidad_id=universidad_id).order_by('id')
        universidades = Universidad.objects.all()
        paginator = Paginator(facultades, OBJ_PER_PAGE)
        page_obj = paginator.get_page(page)

        context = {
            "universidades": universidades,
            "page_obj": page_obj,
        }
        return render(request, self.template_name, context)


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
        facultades_formated = self.facultades_formated()
        context = {
            "facultades": facultades_formated
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = request.POST
        nombre = form['nombre']
        facultad_id = form['facultad']
        EscuelaProfesional.objects.create(nombre=nombre, facultad_id=facultad_id)
        msg = "Datos de escuela profesional guardados"
        facultades_formated = self.facultades_formated()

        context = {
            "facultades": facultades_formated,
            "msg": msg,
        }
        return render(request, self.template_name, context)
    
    def facultades_formated(self):
        facultades = Facultad.objects.all()
        facultades_formated = []
        for facultad in facultades:
            aux = {
                'id': facultad.id,
                'nombre': facultad.nombre,
                'universidad': facultad.universidad.siglas,
            }
            facultades_formated.append(aux)

        return facultades_formated

class ViewEscuelaListar(ListView):
    template_name = 'escuela/listar.html'
    paginate_by = 10
    model = EscuelaProfesional

class ViewEscuelaListadoFiltrar(View):
    template_name = 'escuela/lista_filtrar.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)

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
    template_name = 'examen/listar.html'
    paginate_by = 10
    model = Examen

class ViewExamenListadoFiltrar(View):
    template_name = 'examen/lista_filtrar.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)

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
        nombre = form['nombre']
        siglas = form['siglas']
        Curso.objects.create(nombre=nombre, siglas=siglas)
        msg = "Datos de curso guardados"

        context = {
            "msg": msg
        }
        return render(request, self.template_name, context)

class ViewCursoListar(ListView):
    template_name = 'curso/listar.html'
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
    template_name = 'pregunta/listar.html'
    paginate_by = 10
    model = Pregunta

class ViewPreguntaListadoFiltrar(View):
    template_name = 'pregunta/lista_filtrar.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)

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
    template_name = 'resultado/listar.html'
    paginate_by = 10
    model = ResultadoExamen

class ViewResultadoListadoFiltrar(View):
    template_name = 'resultado/lista_filtrar.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)

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

