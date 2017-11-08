from django.db import models
from decimal import Decimal, DecimalException
from django.core.validators import MinValueValidator
from . import options

class Question(models.Model):

    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    status = models.CharField(max_length=3, null=True)
    #user_question =
    #user_response =
    calification = models.IntegerField(default=0)
    date = models.DateTimeField(editable=False, auto_now=True, null=True)

    def __str__(self):
        return '%s' % self.id


class ImageQuestion(models.Model):
    image = models.ImageField(upload_to='questions')
    id_question = models.ForeignKey(Question)

    def __str__(self):
        return '%s' % self.id


class Specie(models.Model):

    MALE = 'ML'
    FEMALE = 'FM'

    SEX = (
      (MALE, 'Macho'),
      (FEMALE, 'Hembra'),
      )

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

    specie = models.CharField(max_length=10,choices=SPECIES)
    race = models.CharField(max_length=3, null=False)
    age = models.IntegerField(validators=[MinValueValidator(Decimal('0'))])
    gender = models.CharField(max_length=3, choices=SEX, default=MALE)
    weight = models.DecimalField(max_digits=5, decimal_places=3)

    def __str__(self):
        return '%s' % self.id


class Bovine(Specie):
    heart_rate = models.IntegerField(default=0)
    respiratory_rate = models.IntegerField(default=0)
    temperature = models.DecimalField(max_digits=5, decimal_places=3)
    capilar = models.IntegerField(default=0)
    mucosal_color = models.CharField(max_length=30, null=True)
    lymph_nodes = models.CharField(max_length=50, null=True)
    ruminal = models.CharField(max_length=80, null=True)
    body_condition = models.TextField(null=True)

    def __str__(self):
        return '%s' % self.id


class Goat(Specie):
    physiological_stage = models.CharField(max_length=30, null=True)
    zootechnical = models.CharField(max_length=50, null=True)
    production_system = models.CharField(max_length=30, null=True)
    heart_rate = models.IntegerField(default=0)
    respiratory_rate = models.IntegerField(default=0)
    temperature = models.DecimalField(max_digits=5, decimal_places=3)
    capilar = models.IntegerField(default=0)
    mucosal_color = models.CharField(max_length=30, null=True)
    lymph_nodes = models.CharField(max_length=50, null=True)
    ruminal = models.CharField(max_length=80, null=True)
    body_condition = models.TextField(null=True)
    cough = models.BooleanField()
    def __str__(self):
        return '%s' % self.id


class Rabbit(Specie):
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

    productive_stage = models.CharField(max_length=10, choices=PRODUCTIVE, default=LACTATING)
    heart_rate = models.IntegerField(default=0)
    respiratory_rate = models.IntegerField(default=0)
    temperature = models.DecimalField(max_digits=5, decimal_places=3)
    capilar = models.IntegerField(default=0)
    mucosal_color = models.CharField(max_length=30, null=True)
    lymph_nodes = models.CharField(max_length=50, null=True)
    body_condition = models.TextField(null=True)
    dehydration = models.CharField(max_length=50, null=True)

    def __str__(self):
        return '%s' % self.id


class Cat(Specie):
    heart_rate = models.IntegerField(default=0)
    respiratory_rate = models.IntegerField(default=0)
    temperature = models.DecimalField(max_digits=5, decimal_places=3)
    capilar = models.IntegerField(default=0)
    mucosal_color = models.CharField(max_length=30, null=True)
    tusigno_reflex = models.CharField(max_length=30, null=True)
    pulse = models.IntegerField(default=0)
    injuries = models.CharField(max_length=30, null=True)

    def __str__(self):
        return '%s' % self.id


class Ovine(Specie):
    physiological_stage = models.CharField(max_length=30, null=True)
    zootechnical = models.CharField(max_length=50, null=True)
    production_system = models.CharField(max_length=30, null=True)
    heart_rate = models.IntegerField(default=0)
    respiratory_rate = models.IntegerField(default=0)
    temperature = models.DecimalField(max_digits=5, decimal_places=3)
    mucosal_color = models.CharField(max_length=30, null=True)
    lymph_nodes = models.CharField(max_length=50, null=True)
    ruminal = models.CharField(max_length=80, null=True)
    body_condition = models.TextField(null=True)
    cough = models.BooleanField()

    def __str__(self):
        return '%s' % self.id


class Dog(Specie):
    heart_rate = models.IntegerField(default=0)
    respiratory_rate = models.IntegerField(default=0)
    temperature = models.DecimalField(max_digits=5, decimal_places=3)
    mucosal_color = models.CharField(max_length=30, null=True)
    capilar = models.IntegerField(default=0)

    def __str__(self):
        return '%s' % self.id


class Porcine(Specie):
    physiological_stage = models.CharField(max_length=30, null=True)
    production_system = models.CharField(max_length=30, null=True)
    curse = models.CharField(max_length=60, null=True)
    heart_rate = models.IntegerField(default=0)
    respiratory_rate = models.IntegerField(default=0)
    temperature = models.DecimalField(max_digits=5, decimal_places=3)
    body_condition = models.TextField(null=True)
    attitude = models.TextField(null=True)
    color = models.CharField(max_length=30, null=True)

    def __str__(self):
        return '%s' % self.id


class Bee(models.Model):
    pass


class Bird(models.Model):
    type_animal = models.CharField(max_length=60, null=True)
    zootechnical_purpose = models.CharField(max_length=30, null=True)


class Horse(Specie):
    heart_rate = models.IntegerField(default=0)
    respiratory_rate = models.IntegerField(default=0)
    temperature = models.DecimalField(max_digits=5, decimal_places=3)
    capilar = models.IntegerField(default=0)
    mucosal_color = models.CharField(max_length=30, null=True)
    lymph_nodes = models.CharField(max_length=50, null=True)
    body_condition = models.TextField(null=True)

    def __str__(self):
        return '%s' % self.id