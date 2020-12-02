from django.contrib.auth import authenticate, login
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

    def post(self, request, *args, **kwargs):
        form = request.POST
        print(form)
        username = form['username']
        password = form['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home:view_home')

        auth_msg = 'usuario y/o contraseña incorrectos'

        context = {
            'auth_msg': auth_msg,
        }
        return render(request, self.template_name, context)


class ViewHome(View):
    template_name = "home/home.html"

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)
