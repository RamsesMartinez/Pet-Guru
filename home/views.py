from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django

from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView

from .forms import *

from .models import Question
from .models import Specie
from .models import ImageQuestion

from users.models import User

import django_filters


def index(request):
    if request.user.is_authenticated():
        return redirect('home:usuario')

    template = 'index.html'
    message = None
    articles = Question.objects.all()
    f = SpecieFilter(request.GET, queryset=articles)

    login_form = LogInForm(request.POST or None)

    if request.method == 'POST':
        user_log = request.POST['Usuario']
        pass_log = request.POST['Contraseña']
        user_auth = authenticate(username=user_log, password=pass_log)

        if user_auth is not None:
            login_django(request, user_auth)
            return redirect('home:usuario')
        else:
            message = "Usuario o contraseña incorrectos."

    context = {
        'title': "PetGurú - Inicio",
        'message': message,
        'articles': articles,
        'form': login_form,
        'filter': f,
    }
    return render(request, template, context)


def question(request, id=None):
    template = 'question.html'
    instance = get_object_or_404(Question, id=id)
    image = ImageQuestion.objects.filter(id_question=instance.id)
    context = {
        'images': image,
        'titulo': instance.title,
        'instance': instance,
    }

    return render(request, template, context)


def us(request):
    template = 'nosotros.html'
    context = {
        'title': "PetGurú - Nosotros",
    }
    return render(request, template, context)


def rules(request):
    template = 'reglamento.html'
    context = {
        'title': "PetGurú - Reglamento",
    }
    return render(request, template, context)


@login_required(login_url='home:inicio')
def logout(request):
    logout_django(request)
    return redirect('home:inicio')


@login_required(login_url='home:inicio')
def user(request):
    if request.user.rol == 'ST':
        template = 'user.html'
        solved = Question.objects.filter(user_response=request.user.pk)
        articles = Question.objects.all()
        base_form = BaseForm(request.POST or None)
        cow_form = CowForm(request.POST or None)
        porcine_form = PorcineForm(request.POST or None)
        horse_form = HorseForm(request.POST or None)
        goat_form = GoatForm(request.POST or None)
        ovine_form = OvineForm(request.POST or None)
        rabbit_form = RabbitForm(request.POST or None)
        bird_form = BirdForm(request.POST or None)
        dog_form = DogForm(request.POST or None)
        cat_form = CatForm(request.POST or None)
        wild_form = WildForm(request.POST or None)
        aquatic_form = AquaticForm(request.POST or None)
        bee_form = BeeForm(request.POST or None)

        if request.method == 'POST':
            if base_form.is_valid():
                base_form.save()
                if cow_form.is_valid():
                    cow_form.save()
                    return redirect ('home:usuario')

        context = {
            'title': "Bienvenido "+request.user.username,
            'solveds': solved,
            'articles':articles,
            'baseForm': base_form,
            'cow_form': cow_form,
            'porcine_form': porcine_form,
            'horse_form': horse_form,
            'goat_form': goat_form,
            'ovine_form': ovine_form,
            'rabbit_form': rabbit_form,
            'bird_form': bird_form,
            'dog_form': dog_form,
            'cat_form': cat_form,
            'wild_form': wild_form,
            'aquatic_form': aquatic_form,
            'bee_form': bee_form,
        }
        return render(request, template, context)

    elif request.user.rol == 'TC':
        template = 'prof.html'
        solved = Question.objects.filter(user_response=request.user.pk).filter(status='CL')
        article = Question.objects.filter(status='CL')
        context = {
            'title': "Profesional " + request.user.username,
            'solveds': solved,
            'articles': article,
        }
        return render(request, template, context)

    elif request.user.rol == 'AD':
        return redirect('admin:login')


class RegisterUser(CreateView):
    model = User
    template_name = "user_register.html"
    form_class = RegisterForm
    success_url = reverse_lazy('home:usuario') 


class SpecieFilter(django_filters.FilterSet):
    class Meta():
        model = Specie
        fields = ['specie']


def search(request):
    articles = Specie.objects.filter()
    f = SpecieFilter(request.GET, queryset=articles)
    return render(request, 'article.html', {'filt': f})
            