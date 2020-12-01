from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User

from apps.usuario.models import Alumno, Docente

# Create your views here.

class ViewLogin(View):
    template_name = "home/login.html"

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)

    # def post(self, request, *args, **kwargs):
        # context = {}
        # return redirect()


