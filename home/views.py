from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
from django.core.paginator import Paginator

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
# Django static files
from django.contrib.staticfiles.templatetags.staticfiles import static

import django_filters
# Email libraries
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders



def index(request):
    if request.user.is_authenticated():
        return redirect('home:usuario')

    template = 'index.html'
    message = None
    articles = Question.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(articles, 6)
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

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
        solved = Question.objects.filter(user_response=request.user.pk).order_by('-id')
        articles = Question.objects.all().order_by('-id')
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


        page = request.GET.get('page', 1)
        paginator = Paginator(articles, 6)
        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            articles = paginator.page(1)
        except EmptyPage:
            articles = paginator.page(paginator.num_pages)

        if request.method == 'POST':
            if base_form.is_valid() and cow_form.is_valid():
                base = base_form.save(commit=False)
                cow = cow_form.save(commit=False)
                base.user_question = request.user
                base.save()
                cow.question = base
                message = 'Pregunta: '+base.title+'\n consula: '+base.description+\
                        '\n\n\n Especie: '+cow.get_specie_display()+'\n Raza: '+cow.race+\
                        '\n Edad: '+str(cow.age)+'\n Género: '+str(cow.gender)+'\n Peso: '+str(cow.weight)+\
                        '\n Frecuencia cardiaca: '+str(cow.heart_rate)+' lpm'+'\n Frecuencia respiratoria: '+str(cow.respiratory_rate)+\
                        ' rpm'+'\n Temperatura: '+str(cow.temperature)+' °C'+'\n Tiempo de llenado capilar: '+str(cow.capilar)+' segundos'+\
                        '\n Color de mucosas: '+cow.mucosal_color+'\n Linfonodos: '+cow.lymph_nodes+'\n Movimientos ruminales: '+cow.ruminal+\
                        '\n Condición corporal: '+cow.body_condition
                cow.save()
                cowmail(request, message)
                return redirect ('home:usuario')
            elif base_form.is_valid() and porcine_form.is_valid():
                base = base_form.save(commit=False)
                pig = porcine_form.save(commit=False)
                base.user_question = request.user
                base.save()
                pig.question = base
                message = 'Pregunta: '+base.title+'\n consula: '+base.description+\
                        '\n\n\n Especie: '+pig.get_specie_display()+'\n Raza: '+pig.race+\
                        '\n Edad: '+str(pig.age)+'\n Género: '+str(pig.gender)+'\n Peso: '+str(pig.weight)+\
                        '\n Etapa fisiológica: '+pig.physiological_stage+'\n Sistema de producción: '+pig.production_system+\
                        '\n Curso del padecimiento en días: '+pig.curse+\
                        '\n Frecuencia cardiaca: '+str(pig.heart_rate)+' lpm'+'\n Frecuencia respiratoria: '+str(pig.respiratory_rate)+\
                        ' rpm'+'\n Temperatura: '+str(pig.temperature)+' °C'+'\n Color de mucosas: '+pig.color+'\n Actitud: '+pig.attitude+\
                        '\n Condición corporal: '+pig.body_condition
                pig.save()
                pigmail(request, message)
                return redirect ('home:usuario')
            elif base_form.is_valid() and horse_form.is_valid():
                base = base_form.save(commit=False)
                horse = horse_form.save(commit=False)
                base.user_question = request.user
                base.save()
                horse.question = base
                message = 'Pregunta: '+base.title+'\n consula: '+base.description+\
                        '\n\n\n Especie: '+horse.get_specie_display()+'\n Raza: '+horse.race+\
                        '\n Edad: '+str(horse.age)+'\n Género: '+str(horse.gender)+'\n Peso: '+str(horse.weight)+\
                        '\n Frecuencia cardiaca: '+str(horse.heart_rate)+' lpm'+'\n Frecuencia respiratoria: '+str(horse.respiratory_rate)+\
                        ' rpm'+'\n Temperatura: '+str(horse.temperature)+' °C'+'\n Tiempo de llenado capilar: '+str(horse.capilar)+' segundos'+\
                        '\n Color de mucosas: '+horse.mucosal_color+'\n Linfonodos: '+horse.lymph_nodes+\
                        '\n Condición corporal: '+horse.body_condition
                horse.save()
                horsemail(request, message)
                return redirect ('home:usuario')
            elif base_form.is_valid() and ovine_form.is_valid():
                base = base_form.save(commit=False)
                ovine = ovine_form.save(commit=False)
                base.user_question = request.user
                base.save()
                ovine.question = base
                message = 'Pregunta: '+base.title+'\n consula: '+base.description+\
                        '\n\n\n Especie: '+ovine.get_specie_display()+'\n Raza: '+ovine.race+\
                        '\n Edad: '+str(ovine.age)+'\n Género: '+str(ovine.gender)+'\n Peso: '+str(ovine.weight)+\
                        '\n Etapa fisiológica: '+ovine.physiological_stage+'\n Sistema de producción: '+ovine.production_system+\
                        '\n Fin zootécnico: '+ovine.zootechnical+\
                        '\n Frecuencia cardiaca: '+str(ovine.heart_rate)+' lpm'+'\n Frecuencia respiratoria: '+str(ovine.respiratory_rate)+\
                        ' rpm'+'\n Temperatura: '+str(ovine.temperature)+' °C'+'\n Color de mucosas: '+ovine.mucosal_color+'\n Movimientos ruminales: '+ovine.ruminal+\
                        '\n Condición corporal: '+ovine.body_condition
                ovine.save()
                ovinemail(request, message)
                return redirect ('home:usuario')
            elif base_form.is_valid() and goat_form.is_valid():
                base = base_form.save(commit=False)
                goat = goat_form.save(commit=False)
                base.user_question = request.user
                base.save()
                goat.question = base
                message = 'Pregunta: '+base.title+'\n consula: '+base.description+\
                        '\n\n\n Especie: '+pig.get_specie_display()+'\n Raza: '+pig.race+\
                        '\n Edad: '+str(pig.age)+'\n Género: '+str(pig.gender)+'\n Peso: '+str(pig.weight)+\
                        '\n Etapa fisiológica: '+pig.physiological_stage+'\n Sistema de producción: '+pig.production_system+\
                        '\n Curso del padecimiento en días: '+pig.curse+\
                        '\n Frecuencia cardiaca: '+str(pig.heart_rate)+' lpm'+'\n Frecuencia respiratoria: '+str(pig.respiratory_rate)+\
                        ' rpm'+'\n Temperatura: '+str(pig.temperature)+' °C'+'\n Color de mucosas: '+pig.color+'\n Actitud: '+pig.attitude+\
                        '\n Condición corporal: '+pig.body_condition
                goat.save()
                goatmail(request, message)
                return redirect ('home:usuario')
            elif base_form.is_valid() and rabbit_form.is_valid():
                base = base_form.save(commit=False)
                rab = rabbit_form.save(commit=False)
                base.user_question = request.user
                base.save()
                rab.question = base
                message = 'Pregunta: '+base.title+'\n consula: '+base.description+\
                        '\n\n\n Especie: '+pig.get_specie_display()+'\n Raza: '+pig.race+\
                        '\n Edad: '+str(pig.age)+'\n Género: '+str(pig.gender)+'\n Peso: '+str(pig.weight)+\
                        '\n Etapa fisiológica: '+pig.physiological_stage+'\n Sistema de producción: '+pig.production_system+\
                        '\n Curso del padecimiento en días: '+pig.curse+\
                        '\n Frecuencia cardiaca: '+str(pig.heart_rate)+' lpm'+'\n Frecuencia respiratoria: '+str(pig.respiratory_rate)+\
                        ' rpm'+'\n Temperatura: '+str(pig.temperature)+' °C'+'\n Color de mucosas: '+pig.color+'\n Actitud: '+pig.attitude+\
                        '\n Condición corporal: '+pig.body_condition
                rab.save()
                rabbitmail(request, message)
                return redirect ('home:usuario')
            elif base_form.is_valid() and bird_form.is_valid():
                base = base_form.save(commit=False)
                bird = bird_form.save(commit=False)
                base.user_question = request.user
                base.save()
                bird.question = base
                message = 'Pregunta: '+base.title+'\n consula: '+base.description+\
                        '\n\n\n Especie: '+pig.get_specie_display()+'\n Raza: '+pig.race+\
                        '\n Edad: '+str(pig.age)+'\n Género: '+str(pig.gender)+'\n Peso: '+str(pig.weight)+\
                        '\n Etapa fisiológica: '+pig.physiological_stage+'\n Sistema de producción: '+pig.production_system+\
                        '\n Curso del padecimiento en días: '+pig.curse+\
                        '\n Frecuencia cardiaca: '+str(pig.heart_rate)+' lpm'+'\n Frecuencia respiratoria: '+str(pig.respiratory_rate)+\
                        ' rpm'+'\n Temperatura: '+str(pig.temperature)+' °C'+'\n Color de mucosas: '+pig.color+'\n Actitud: '+pig.attitude+\
                        '\n Condición corporal: '+pig.body_condition
                bird.save()
                birdmail(request, message)
                return redirect ('home:usuario')
            elif base_form.is_valid() and dog_form.is_valid():
                base = base_form.save(commit=False)
                dog = dog_form.save(commit=False)
                base.user_question = request.user
                base.save()
                dog.question = base
                message = 'Pregunta: '+base.title+'\n consula: '+base.description+\
                        '\n\n\n Especie: '+pig.get_specie_display()+'\n Raza: '+pig.race+\
                        '\n Edad: '+str(pig.age)+'\n Género: '+str(pig.gender)+'\n Peso: '+str(pig.weight)+\
                        '\n Etapa fisiológica: '+pig.physiological_stage+'\n Sistema de producción: '+pig.production_system+\
                        '\n Curso del padecimiento en días: '+pig.curse+\
                        '\n Frecuencia cardiaca: '+str(pig.heart_rate)+' lpm'+'\n Frecuencia respiratoria: '+str(pig.respiratory_rate)+\
                        ' rpm'+'\n Temperatura: '+str(pig.temperature)+' °C'+'\n Color de mucosas: '+pig.color+'\n Actitud: '+pig.attitude+\
                        '\n Condición corporal: '+pig.body_condition
                dog.save()
                dogmail(request, message)
                return redirect ('home:usuario')
            elif base_form.is_valid() and cat_form.is_valid():
                base = base_form.save(commit=False)
                cat = cat_form.save(commit=False)
                base.user_question = request.user
                base.save()
                cat.question = base
                message = 'Pregunta: '+base.title+'\n consula: '+base.description+\
                        '\n\n\n Especie: '+pig.get_specie_display()+'\n Raza: '+pig.race+\
                        '\n Edad: '+str(pig.age)+'\n Género: '+str(pig.gender)+'\n Peso: '+str(pig.weight)+\
                        '\n Etapa fisiológica: '+pig.physiological_stage+'\n Sistema de producción: '+pig.production_system+\
                        '\n Curso del padecimiento en días: '+pig.curse+\
                        '\n Frecuencia cardiaca: '+str(pig.heart_rate)+' lpm'+'\n Frecuencia respiratoria: '+str(pig.respiratory_rate)+\
                        ' rpm'+'\n Temperatura: '+str(pig.temperature)+' °C'+'\n Color de mucosas: '+pig.color+'\n Actitud: '+pig.attitude+\
                        '\n Condición corporal: '+pig.body_condition
                cat.save()
                catmail(request, message)
                return redirect ('home:usuario')
            elif base_form.is_valid() and wild_form.is_valid():
                base = base_form.save(commit=False)
                wild = wild_form.save(commit=False)
                base.user_question = request.user
                base.save()
                wild.question = base
                message = 'Pregunta: '+base.title+'\n consula: '+base.description+\
                        '\n\n\n Especie: '+pig.get_specie_display()+'\n Raza: '+pig.race+\
                        '\n Edad: '+str(pig.age)+'\n Género: '+str(pig.gender)+'\n Peso: '+str(pig.weight)+\
                        '\n Etapa fisiológica: '+pig.physiological_stage+'\n Sistema de producción: '+pig.production_system+\
                        '\n Curso del padecimiento en días: '+pig.curse+\
                        '\n Frecuencia cardiaca: '+str(pig.heart_rate)+' lpm'+'\n Frecuencia respiratoria: '+str(pig.respiratory_rate)+\
                        ' rpm'+'\n Temperatura: '+str(pig.temperature)+' °C'+'\n Color de mucosas: '+pig.color+'\n Actitud: '+pig.attitude+\
                        '\n Condición corporal: '+pig.body_condition
                wild.save()
                wildmail(request, message)
                return redirect ('home:usuario')
            elif base_form.is_valid() and aquatic_form.is_valid():
                base = base_form.save(commit=False)
                aq = aquatic_form.save(commit=False)
                base.user_question = request.user
                base.save()
                aq.question = base
                message = 'Pregunta: '+base.title+'\n consula: '+base.description+\
                        '\n\n\n Especie: '+pig.get_specie_display()+'\n Raza: '+pig.race+\
                        '\n Edad: '+str(pig.age)+'\n Género: '+str(pig.gender)+'\n Peso: '+str(pig.weight)+\
                        '\n Etapa fisiológica: '+pig.physiological_stage+'\n Sistema de producción: '+pig.production_system+\
                        '\n Curso del padecimiento en días: '+pig.curse+\
                        '\n Frecuencia cardiaca: '+str(pig.heart_rate)+' lpm'+'\n Frecuencia respiratoria: '+str(pig.respiratory_rate)+\
                        ' rpm'+'\n Temperatura: '+str(pig.temperature)+' °C'+'\n Color de mucosas: '+pig.color+'\n Actitud: '+pig.attitude+\
                        '\n Condición corporal: '+pig.body_condition
                aq.save()
                fishmail(request, message)
                return redirect ('home:usuario')
            elif base_form.is_valid() and bee_form.is_valid():
                base = base_form.save(commit=False)
                bee = bee_form.save(commit=False)
                base.user_question = request.user
                base.save()
                bee.question = base
                message = 'Pregunta: '+base.title+'\n consula: '+base.description+\
                        '\n\n\n Especie: '+pig.get_specie_display()+'\n Raza: '+pig.race+\
                        '\n Edad: '+str(pig.age)+'\n Género: '+str(pig.gender)+'\n Peso: '+str(pig.weight)+\
                        '\n Etapa fisiológica: '+pig.physiological_stage+'\n Sistema de producción: '+pig.production_system+\
                        '\n Curso del padecimiento en días: '+pig.curse+\
                        '\n Frecuencia cardiaca: '+str(pig.heart_rate)+' lpm'+'\n Frecuencia respiratoria: '+str(pig.respiratory_rate)+\
                        ' rpm'+'\n Temperatura: '+str(pig.temperature)+' °C'+'\n Color de mucosas: '+pig.color+'\n Actitud: '+pig.attitude+\
                        '\n Condición corporal: '+pig.body_condition
                bee.save()
                beemail(request, message)
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
        solved = Question.objects.filter(user_response=request.user.pk).filter(Q(status='OP') | Q(status='RP')).order_by('-id')
        article = Question.objects.filter(status='CL').order_by('-id')
        avg = 0

        page = request.GET.get('page', 1)
        paginator = Paginator(solved, 6)
        try:
            solved = paginator.page(page)
        except PageNotAnInteger:
            solved = paginator.page(1)
        except EmptyPage:
            solved = paginator.page(paginator.num_pages)

        qualifications = []
        for qualification in article:
            qualifications.append(qualification.calification)
            if qualifications != 0:
                avg = sum(qualifications) / len(qualifications)
            else:
                avg = 0
        context = {
            'title': "Profesional " + request.user.username,
            'solveds': solved,
            'articles': article,
            'avg': avg,
        }
        return render(request, template, context)

    elif request.user.rol == 'AD':
        return redirect('home:register')


@login_required(login_url='home:inicio')
def register(request):
    if request.user.rol == 'AD':
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
    else:
        return redirect('home:inicio')

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


def cowmail (request, message):
    fromaddr = "itzli2000@gmail.com"
    toaddr = "itzli2000@msn.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Se ha creado una nueva pregunta"

    body = message
    msg.attach(MIMEText(body, 'plain'))
 
    # filename = "main.jpg"
    # attachment = open("C:/Users/Itzli/Documents/GitHub/Pet-Guru/pet_guru/static/images/", "rb")

    # part = MIMEBase('application', 'octet-stream')
    # part.set_payload((attachment).read())
    # encoders.encode_base64(part)
    # part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
     
    # msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "molinona&9")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

    return None


def pigmail (request, message):
    fromaddr = "itzli2000@gmail.com"
    toaddr = "jonathanbasilio24@outlook.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Se ha creado una nueva pregunta"

    body = message
    msg.attach(MIMEText(body, 'plain'))
 
    # filename = "main.jpg"
    # attachment = open("C:/Users/Itzli/Documents/GitHub/Pet-Guru/pet_guru/static/images/", "rb")

    # part = MIMEBase('application', 'octet-stream')
    # part.set_payload((attachment).read())
    # encoders.encode_base64(part)
    # part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
     
    # msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "molinona&9")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

    return None


def horsemail (request, message):
    fromaddr = "itzli2000@gmail.com"
    toaddr = "itzli2000@msn.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Se ha creado una nueva pregunta"

    body = message
    msg.attach(MIMEText(body, 'plain'))
 
    # filename = "main.jpg"
    # attachment = open("C:/Users/Itzli/Documents/GitHub/Pet-Guru/pet_guru/static/images/", "rb")

    # part = MIMEBase('application', 'octet-stream')
    # part.set_payload((attachment).read())
    # encoders.encode_base64(part)
    # part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
     
    # msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "molinona&9")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

    return None


def ovinemail (request, message):
    fromaddr = "itzli2000@gmail.com"
    toaddr = "itzli2000@msn.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Se ha creado una nueva pregunta"

    body = message
    msg.attach(MIMEText(body, 'plain'))
 
    # filename = "main.jpg"
    # attachment = open("C:/Users/Itzli/Documents/GitHub/Pet-Guru/pet_guru/static/images/", "rb")

    # part = MIMEBase('application', 'octet-stream')
    # part.set_payload((attachment).read())
    # encoders.encode_base64(part)
    # part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
     
    # msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "molinona&9")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

    return None


def goatmail (request, message):
    fromaddr = "itzli2000@gmail.com"
    toaddr = "itzli2000@msn.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Se ha creado una nueva pregunta"

    body = message
    msg.attach(MIMEText(body, 'plain'))
 
    # filename = "main.jpg"
    # attachment = open("C:/Users/Itzli/Documents/GitHub/Pet-Guru/pet_guru/static/images/", "rb")

    # part = MIMEBase('application', 'octet-stream')
    # part.set_payload((attachment).read())
    # encoders.encode_base64(part)
    # part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
     
    # msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "molinona&9")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

    return None


def rabbitmail (request, message):
    fromaddr = "itzli2000@gmail.com"
    toaddr = "itzli2000@msn.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Se ha creado una nueva pregunta"

    body = message
    msg.attach(MIMEText(body, 'plain'))
 
    # filename = "main.jpg"
    # attachment = open("C:/Users/Itzli/Documents/GitHub/Pet-Guru/pet_guru/static/images/", "rb")

    # part = MIMEBase('application', 'octet-stream')
    # part.set_payload((attachment).read())
    # encoders.encode_base64(part)
    # part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
     
    # msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "molinona&9")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

    return None


def birdmail (request, message):
    fromaddr = "itzli2000@gmail.com"
    toaddr = "itzli2000@msn.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Se ha creado una nueva pregunta"

    body = message
    msg.attach(MIMEText(body, 'plain'))
 
    # filename = "main.jpg"
    # attachment = open("C:/Users/Itzli/Documents/GitHub/Pet-Guru/pet_guru/static/images/", "rb")

    # part = MIMEBase('application', 'octet-stream')
    # part.set_payload((attachment).read())
    # encoders.encode_base64(part)
    # part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
     
    # msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "molinona&9")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

    return None


def dogmail (request, message):
    fromaddr = "itzli2000@gmail.com"
    toaddr = "itzli2000@msn.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Se ha creado una nueva pregunta"

    body = message
    msg.attach(MIMEText(body, 'plain'))
 
    # filename = "main.jpg"
    # attachment = open("C:/Users/Itzli/Documents/GitHub/Pet-Guru/pet_guru/static/images/", "rb")

    # part = MIMEBase('application', 'octet-stream')
    # part.set_payload((attachment).read())
    # encoders.encode_base64(part)
    # part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
     
    # msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "molinona&9")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

    return None


def catmail (request, message):
    fromaddr = "itzli2000@gmail.com"
    toaddr = "itzli2000@msn.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Se ha creado una nueva pregunta"

    body = message
    msg.attach(MIMEText(body, 'plain'))
 
    # filename = "main.jpg"
    # attachment = open("C:/Users/Itzli/Documents/GitHub/Pet-Guru/pet_guru/static/images/", "rb")

    # part = MIMEBase('application', 'octet-stream')
    # part.set_payload((attachment).read())
    # encoders.encode_base64(part)
    # part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
     
    # msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "molinona&9")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

    return None


def wildmail (request, message):
    fromaddr = "itzli2000@gmail.com"
    toaddr = "itzli2000@msn.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Se ha creado una nueva pregunta"

    body = message
    msg.attach(MIMEText(body, 'plain'))
 
    # filename = "main.jpg"
    # attachment = open("C:/Users/Itzli/Documents/GitHub/Pet-Guru/pet_guru/static/images/", "rb")

    # part = MIMEBase('application', 'octet-stream')
    # part.set_payload((attachment).read())
    # encoders.encode_base64(part)
    # part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
     
    # msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "molinona&9")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

    return None


def fishmail (request, message):
    fromaddr = "itzli2000@gmail.com"
    toaddr = "itzli2000@msn.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Se ha creado una nueva pregunta"

    body = message
    msg.attach(MIMEText(body, 'plain'))
 
    # filename = "main.jpg"
    # attachment = open("C:/Users/Itzli/Documents/GitHub/Pet-Guru/pet_guru/static/images/", "rb")

    # part = MIMEBase('application', 'octet-stream')
    # part.set_payload((attachment).read())
    # encoders.encode_base64(part)
    # part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
     
    # msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "molinona&9")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

    return None


def beemail (request, message):
    fromaddr = "itzli2000@gmail.com"
    toaddr = "itzli2000@msn.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Se ha creado una nueva pregunta"

    body = message
    msg.attach(MIMEText(body, 'plain'))
 
    # filename = "main.jpg"
    # attachment = open("C:/Users/Itzli/Documents/GitHub/Pet-Guru/pet_guru/static/images/", "rb")

    # part = MIMEBase('application', 'octet-stream')
    # part.set_payload((attachment).read())
    # encoders.encode_base64(part)
    # part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
     
    # msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "molinona&9")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

    return None