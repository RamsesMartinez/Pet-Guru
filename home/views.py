from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
from django.http import JsonResponse, HttpResponse
from django.views.generic import CreateView

from django.http import HttpResponse
from .models import Question
from .forms import VacaForm, Login
# Create your views here.


def index(request):
    if request.user.is_authenticated():
        return redirect('home:usuario')

    message = None
    Login_form = Login(request.POST or None)
    
    if request.method == 'POST':
        userLog = request.POST['username']
        passLog = request.POST['password']
        user = authenticate( username = userLog , password = passLog)
        if user is not None:
            login_django(request, user)
            return redirect('home:usuario')
        else:
            message = "Usuario o contraseña incorrectos."

    context = {
        'title': "PetGurú - Inicio",
        'message' : message,
        'form' : Login_form,
    }
    template = 'index.html'
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


@login_required(login_url='home:inicio')
def user(request):
    template = 'user.html'
    User = None
    if request.user.is_authenticated():
        User = request.user.username
    my_form = VacaForm(request.POST or None)
    if request.method == 'POST':
        if my_form.is_valid():
            my_form.save()
            return redirect ('home:usuario')

    context={       
        'title': "PetGurú - Bienvenido",
        'form': my_form,
        'user': User,
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
