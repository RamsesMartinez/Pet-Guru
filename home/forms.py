from django import forms
from django.forms import ModelForm 
from .models import Question

class VacaForm(ModelForm):
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

class Login(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20, widget = forms.PasswordInput())