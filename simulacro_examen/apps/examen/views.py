from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from simulacro_examen.settings import OBJ_PER_PAGE

from apps.examen.forms import PreguntaForm
from apps.examen.models import Universidad, Facultad, EscuelaProfesional, Examen, ExamenPregunta, Curso, CursoExamen, Pregunta, Alternativa, ResultadoExamen
from apps.usuario.models import Alumno, Docente


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
        facultades = Facultad.objects.filter(
            universidad_id=universidad_id).order_by('id')
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


class APIGetFacultadesByUniversidadId(View):
    def get(self, request, *args, **kwargs):
        universidad_id = kwargs['universidad_id']
        facultades = Facultad.objects.filter(universidad_id=universidad_id)

        facultades_json = []
        for facultad in facultades:
            facultad_json = {
                "id": facultad.id,
                "nombre": facultad.nombre,
            }
            facultades_json.append(facultad_json)

        return JsonResponse(facultades_json, safe=False)


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
        EscuelaProfesional.objects.create(
            nombre=nombre, facultad_id=facultad_id)
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
        universidades = Universidad.objects.all()
        context = {
            "universidades": universidades
        }
        return render(request, self.template_name, context)


class ViewEscuelaFiltrarPages(View):
    template_name = 'escuela/lista_filtrar.html'

    def get(self, request, *args, **kwargs):
        page = request.GET['page']
        facultad_id = kwargs['facultad_pk']
        escuelas = EscuelaProfesional.objects.filter(
            facultad_id=facultad_id).order_by('id')
        universidades = Universidad.objects.all()
        paginator = Paginator(escuelas, OBJ_PER_PAGE)
        page_obj = paginator.get_page(page)

        context = {
            'universidades': universidades,
            'page_obj': page_obj,
        }
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
        universidades = Universidad.objects.all()
        cursos = Curso.objects.all()
        docentes = Docente.objects.all()

        context = {
            'universidades': universidades,
            'cursos': cursos,
            'docentes': docentes,
        }
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
        universidades = Universidad.objects.all()
        context = {
            "universidades": universidades,
        }
        return render(request, self.template_name, context)


class ViewExamenFiltrarPages(View):
    template_name = 'examen/lista_filtrar.html'

    def get(self, request, *args, **kwargs):
        page = request.GET['page']
        universidad_id = kwargs['universidad_pk']
        examenes = Examen.objects.filter(
            universidad_id=universidad_id).order_by('id')
        universidades = Universidad.objects.all()
        paginator = Paginator(examenes, OBJ_PER_PAGE)
        page_obj = paginator.get_page(page)

        context = {
            "universidades": universidades,
            "page_obj": page_obj,
        }
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

class APIGetCursosByUniversidadId(View):
    def get(self, request, *args, **kwargs):
        universidad_pk = kwargs['universidad_pk']
        cursos = Curso.objects.filter(universidad_id=universidad_pk)

        cursos_json = []
        for curso in cursos:
            cursos_json.append(cursos)

        return JsonResponse(cursos_json, safe=False)


class ViewPreguntaNuevo(View):
    template_name = 'pregunta/nuevo.html'

    def get(self, request, *args, **kwargs):
        form = PreguntaForm()
        context = {
            "form": form,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        alt1 = request.POST['alt1']
        alt2 = request.POST['alt2']
        alt3 = request.POST['alt3']
        alt4 = request.POST['alt4']
        alt5 = request.POST['alt5']

        form = PreguntaForm(request.POST)
        if form.is_valid():
            pregunta = form.save()
            altObj1 = Alternativa.objects.create(
                alternativa=alt1, correcta=True, pregunta=pregunta)
            altObj2 = Alternativa.objects.create(
                alternativa=alt2, pregunta=pregunta)
            altObj3 = Alternativa.objects.create(
                alternativa=alt3, pregunta=pregunta)
            altObj4 = Alternativa.objects.create(
                alternativa=alt4, pregunta=pregunta)
            altObj5 = Alternativa.objects.create(
                alternativa=alt5, pregunta=pregunta)
            form = PreguntaForm()

        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class ViewPreguntaListar(ListView):
    template_name = 'pregunta/listar.html'
    paginate_by = 10
    model = Pregunta


class ViewPreguntaListadoFiltrar(View):
    template_name = 'pregunta/lista_filtrar.html'

    def get(self, request, *args, **kwargs):
        cursos = Curso.objects.all()
        context = {
            "cursos": cursos
        }
        return render(request, self.template_name, context)


class ViewPreguntaFiltrarPages(View):
    template_name = 'pregunta/lista_filtrar.html'

    def get(self, request, *args, **kwargs):
        page = request.GET['page']
        curso_id = kwargs['curso_id']
        preguntas = Pregunta.objects.filter(curso_id=curso_id).order_by('id')
        cursos = Curso.objects.all()
        paginator = Paginator(preguntas, OBJ_PER_PAGE)
        page_obj = paginator.get_page(page)

        context = {
            "cursos": cursos,
            "page_obj": page_obj,
        }
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


class APIGetPreguntasByDocenteCursoPregunta(View):
    def get(self, request, *args, **kwargs):
        docente_pk = kwargs['docente_pk']
        curso_pk = kwargs['curso_pk']
        nombre_pregunta = kwargs['nombre_pregunta']

        preguntas = Pregunta.objects.filter()

        preguntas_json = []
        for pregunta in preguntas:
            preguntas_json = {
            }
            preguntas_json.append(preguntas_json)

        return JsonResponse(preguntas_json, safe=False)


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
        universidades = Universidad.objects.all()
        context = {
            "universidades": universidades,
        }
        return render(request, self.template_name, context)


class ViewResultadoFiltrarPages(View):
    template_name = 'resultado/lista_filtrar.html'

    def get(self, request, *args, **kwargs):
        page = request.GET['page']
        universidad_id = kwargs['universidad_id']
        alumno = Alumno.objects.filter(usuario=request.user)
        if not alumno[0]:
            # return 404
            return 404

        resultados = ResultadoExamen.objects.filter(
            alumno=alumno,
            universidad_id=universidad_id
        ).order_by('id')

        universidades = Universidad.objects.all()
        paginator = Paginator(resultados, OBJ_PER_PAGE)
        page_obj = paginator.get_page(page)

        context = {
            "universidades": universidades,
            "page_obj": page_obj,
        }
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
