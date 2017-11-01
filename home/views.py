from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
from django.http import JsonResponse, HttpResponse
from django.views.generic import CreateView

from django.http import HttpResponse
from .models import Question
from .forms import AnimalesForm
# Create your views here.

def index(request):
    if request.method == 'POST':

        email = json.loads(request.POST.get('email'))
        password = json.loads(request.POST.get('password'))

        user = authenticate(request, username='Rich', password=password)
        if user is not None:
            login_django(request, user)
            # Redirect to a success page.
            data = {
                'check': "valido"
            }
            print("Valido")
            return JsonResponse(data)
        else:
            # Return an 'invalid login' error message.
            print("No valido")
            data = {
                'check': "No valido"
            }
            return JsonResponse(data)

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
    context = {
        'title': "PetGurú - Nosotros",
    }
    return render(request, template, context)


def reglamento(request):
    template = 'reglamento.html'
    context = {
        'title': "PetGurú - Reglamento",
    }
    return render(request, template, context)


def question(request):
    template = 'single-question.html'
    context = {
        'title': "PetGurú - Pregúnta",
    }
    return render(request, template, context)


@login_required(login_url='home:inicio')
def logout(request):
    logout_django(request)
    return redirect('home:inicio')

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
