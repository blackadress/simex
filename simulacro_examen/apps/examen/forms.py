from django import forms

from apps.examen.models import Pregunta

class PreguntaForm(forms.ModelForm):
    class Meta:
        model = Pregunta
        fields = ('nombre', 'curso', 'docente', 'contenido',)

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'curso': forms.Select(attrs={'class': 'form-control'}),
            'docente': forms.Select(attrs={'class': 'form-control'}),
            'contenido': forms.TextInput(attrs={'class': 'form-control'}),
        }
