from django.shortcuts import render
from django.views import View

# Create your views here.

# VISTAS
class ViewUsuario(View):
    template_name = 'base.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)
