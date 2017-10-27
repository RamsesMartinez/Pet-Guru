from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView

from django.http import HttpResponse
from .models import Question

# Create your views here.
def index(request):
    template = 'index.html'    
    context={    	
    	'title': "PetGurú - Inicio",
    }
    return render(request, template, context)

def nosotros(request):
    template = 'nosotros.html'    
    context={    	
    	'title': "PetGurú - Nosotros",
    }
    return render(request, template, context)

def reglamento(request):
    template = 'reglamento.html'    
    context={    	
    	'title': "PetGurú - Reglamento",
    }
    return render(request, template, context)

def question(request):
    template = 'single-question.html'    
    context={       
        'title': "PetGurú - Pregúnta",
    }
    return render(request, template, context)

class NuevaPregunta(CreateView):
    model = Question
    fields = [
        'especie',
        'pregunta',
        'informacion',
        'edad',
        'peso',
        'sexo',
        'fisiologico',
        'motivo',
        'cardiaca',
        'respiratoria',
        'temperatura',
        'llenado',
        'mucosas',
        'linfonodos',
        'ruminales',
        'clinica'
    ]
    template_name = 'question/nueva_pregunta'

    def form_valid(self, form):
        self.object = form.save()
        return index()