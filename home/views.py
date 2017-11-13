from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django

from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q

from .forms import *

from .models import Question
from .models import Specie
from .models import ImageQuestion

from users.models import User
from django.core.mail import send_mail

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
        'CN': "listo esto funciona",
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
            # subject = 'Se ha creado una pregunta'
            # from_email = settings.EMAIL_HOST_USER
            # to_email = ['itzli2000@msn.com']
            # message = 'Mensaje prueba'
            # send_mail(subject=subject, from_email=from_email, recipient_list=to_email, message=message,
            #           fail_silently=False)
            if base_form.is_valid() and cow_form.is_valid():
                base = base_form.save(commit=False)
                cow = cow_form.save(commit=False)
                base.user_question = request.user
                base.save()
                cow.question = base
                cow.save()
                return redirect ('home:usuario')
            elif base_form.is_valid() and porcine_form.is_valid():
                base = base_form.save(commit=False)
                pig = porcine_form.save(commit=False)
                base.user_question = request.user
                base.save()
                pig.question = base
                pig.save()
                return redirect ('home:usuario')
            elif base_form.is_valid() and horse_form.is_valid():
                base = base_form.save(commit=False)
                horse = horse_form.save(commit=False)
                base.user_question = request.user
                base.save()
                horse.question = base
                horse.save()
                return redirect ('home:usuario')
            elif base_form.is_valid() and ovine_form.is_valid():
                base = base_form.save(commit=False)
                ovine = ovine_form.save(commit=False)
                base.user_question = request.user
                base.save()
                ovine.question = base
                ovine.save()
                return redirect ('home:usuario')
            elif base_form.is_valid() and goat_form.is_valid():
                base = base_form.save(commit=False)
                goat = goat_form.save(commit=False)
                base.user_question = request.user
                base.save()
                goat.question = base
                goat.save()
                return redirect ('home:usuario')
            elif base_form.is_valid() and rabbit_form.is_valid():
                base = base_form.save(commit=False)
                rab = rabbit_form.save(commit=False)
                base.user_question = request.user
                base.save()
                rab.question = base
                rab.save()
                return redirect ('home:usuario')
            elif base_form.is_valid() and bird_form.is_valid():
                base = base_form.save(commit=False)
                bird = bird_form.save(commit=False)
                base.user_question = request.user
                base.save()
                bird.question = base
                bird.save()
                return redirect ('home:usuario')
            elif base_form.is_valid() and dog_form.is_valid():
                base = base_form.save(commit=False)
                dog = dog_form.save(commit=False)
                base.user_question = request.user
                base.save()
                dog.question = base
                dog.save()
                return redirect ('home:usuario')
            elif base_form.is_valid() and cat_form.is_valid():
                base = base_form.save(commit=False)
                cat = cat_form.save(commit=False)
                base.user_question = request.user
                base.save()
                cat.question = base
                cat.save()
                return redirect ('home:usuario')
            elif base_form.is_valid() and wild_form.is_valid():
                base = base_form.save(commit=False)
                wild = wild_form.save(commit=False)
                base.user_question = request.user
                base.save()
                wild.question = base
                wild.save()
                return redirect ('home:usuario')
            elif base_form.is_valid() and aquatic_form.is_valid():
                base = base_form.save(commit=False)
                aq = aquatic_form.save(commit=False)
                base.user_question = request.user
                base.save()
                aq.question = base
                aq.save()
                return redirect ('home:usuario')
            elif base_form.is_valid() and bee_form.is_valid():
                base = base_form.save(commit=False)
                bee = bee_form.save(commit=False)
                base.user_question = request.user
                base.save()
                bee.question = base
                bee.save()
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
        solved = Question.objects.filter(user_response=request.user.pk).filter(Q(status='OP') | Q(status='RP'))
        article = Question.objects.filter(status='CL')
        qualifications = []
        for qualification in article:
            qualifications.append(qualification.calification)
        avg = sum(qualifications) / len(qualifications)
        context = {
            'title': "Profesional " + request.user.username,
            'solveds': solved,
            'articles': article,
            'avg': avg,
        }
        return render(request, template, context)

    elif request.user.rol == 'AD':
        return redirect('admin:login')


# def register(request):
#     template = "user_register.html"
#     form_class = RegisterForm(request.POST or None)
#     context = {
#         'title': 'Registro de usuarios',
#         'form': form_class,
#     }
#     if request.method == 'POST':
#         if form_class.is_valid():
#             form = form_class.save(commit=False)
#             form.setpassword(form.password1)
#             form.save()
#     return render(request, template, context)


def register(request):
    template = "user_register.html"
    f = RegisterForm()
    messages = None
    context = {
        'title': 'Registro de usuarios',
        'form': f,
    }
    if request.method == 'POST':
        f = RegisterForm(request.POST)
        if f.is_valid():
            f.save()
            messages='Usuario creado correctamente'
            return redirect('home:register')

    return render(request, template, context)



class SpecieFilter(django_filters.FilterSet):
    class Meta():
        model = Specie
        fields = ['specie']


def search(request):
    articles = Specie.objects.filter()
    f = SpecieFilter(request.GET, queryset=articles)
    context = {
        'filt': f,
        'articles': articles
    }
    return render(request, 'article.html', context)