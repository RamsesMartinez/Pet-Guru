from django.db import models
from . import options

class Question(models.Model):
    BOVINO = 'BV'
    PORCINO  = 'PR'
    EQUINO  = 'EQ'
    OVINO = 'OV'
    CAPRINO = 'CP'
    LEPORIDO = 'LP'
    AVE = 'AV'
    CANINO = 'CN'
    FELINO = 'FL'
    SILVESTRE = 'SL'
    ABEJA = 'BJ'

    SPECIES = (
      (BOVINO, 'Bovino'),
      (PORCINO, 'Porcino'),
      (EQUINO, 'Equino'),
      (OVINO, 'Ovino'),
      (CAPRINO, 'Caprino'),
      (LEPORIDO, 'Lepórido'),
      (AVE, 'Ave'),
      (CANINO, 'Canino'),
      (FELINO, 'Felino'),
      (SILVESTRE, 'Silvestre'),
      (ABEJA, 'Abeja'),
      )


    MALE = 'ML'
    FEMALE = 'FM'

    SEX = (
      (MALE, 'Macho'),
      (FEMALE, 'Hembra'),
      )

    LACTATING = 'LC'
    PREGNANT = 'PG'
    INCREASE = 'IC'
    FATTEN = 'FT'

    PRODUCTIVE = (
      (LACTATING, 'Lactante'),
      (PREGNANT, 'Gestante'),
      (INCREASE, 'Crecimiento'),
      (FATTEN, 'Engorda'),
      )

    #user = models.ForeignKey(User)
    especie = models.CharField(max_length=3, choices=SPECIES, default='')
    pregunta = models.CharField(max_length=100, default='')
    informacion = models.TextField(default='', blank=True, null=True)
    edad = models.CharField(max_length=2,default=0)
    peso = models.CharField(max_length=10,default=0)
    sexo = models.CharField(max_length=3, choices=SEX, default=MALE)
    fisiologico = models.CharField(max_length=3, choices=PRODUCTIVE, default=LACTATING)
    motivo = models.CharField(max_length=100, default='')
    cardiaco = models.CharField(max_length=10,default=0)
    respiratorio = models.CharField(max_length=10,default=0)
    temperatura = models.CharField(max_length=3,default=0)
    llenado = models.CharField(max_length=100, default='')
    mucosas = models.CharField(max_length=100, default='')
    linfonodos = models.CharField(max_length=100, default='')
    clinica = models.TextField(default='', blank=True, null=True)
    date = models.DateTimeField(editable=False, auto_now=True, null=True)
    image = models.ImageField(upload_to='questions', blank=True, null=True)

    def __str__(self):
        return '%s' % self.id
