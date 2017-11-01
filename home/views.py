from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView

from django.http import HttpResponse
from .models import Question
from .forms import AnimalesForm
# Create your views here.
def index(request):
    template = 'index.html'
    my_form = AnimalesForm(request.POST or None)
    if request.method == 'POST':
        if my_form.is_valid():
            my_form.save()
            return redirect ('home:inicio')

    context={    	
    	'title': "PetGurú - Inicio",
        'form': my_form,
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



# No usada hasta el momento
# class NuevaPregunta(CreateView):
#     model = Question
#     fields = [
#         'especie',
#         'pregunta',
#         'informacion',
#         'edad',
#         'peso',
#         'sexo',
#         'fisiologico',
#         'motivo',
#         'cardiaca',
#         'respiratoria',
#         'temperatura',
#         'llenado',
#         'mucosas',
#         'linfonodos',
#         'ruminales',
#         'clinica',
#         'imagen'
#     ]
#     template_name = 'question/cow.html'

#     def form_valid(self, form):
#         self.object = form.save()
#         return redirect('home:reglamento')