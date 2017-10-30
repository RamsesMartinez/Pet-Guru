from django.forms import ModelForm 
from .models import Question

class AnimalesForm(ModelForm):
    class Meta:
        model = Question
        # Acontinuacion colocamos los campos que quremos que use el form...
        fields = (
          'especie',
          'pregunta',
          'informacion',
          'edad',
          'peso',
          'sexo',
          'fisiologico',
          'motivo',
          'cardiaco',
          'respiratorio',
          'temperatura',
          'llenado',
          'mucosas',
          'linfonodos',
          'clinica',
          'image',
        )