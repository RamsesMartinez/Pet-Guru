from django.db import models
from . import options

class Question(models.Model):
    # BOVINO = 'BV'
    # PORCINO  = 'PR'
    # EQUINO  = 'EQ'
    # OVINO = 'OV'
    # CAPRINO = 'CP'
    # LEPORIDO = 'LP'
    # AVE = 'AV'
    # CANINO = 'CN'
    # FELINO = 'FL'
    # SILVESTRE = 'SL'
    # ABEJA = 'BJ'

    # SPECIES = (
    #   (BOVINO, 'Bovino'),
    #   (PORCINO, 'Porcino'),
    #   (EQUINO, 'Equino'),
    #   (OVINO, 'Ovino'),
    #   (CAPRINO, 'Caprino'),
    #   (LEPORIDO, 'Lepórido'),
    #   (AVE, 'Ave'),
    #   (CANINO, 'Canino'),
    #   (FELINO, 'Felino'),
    #   (SILVESTRE, 'Silvestre'),
    #   (ABEJA, 'Abeja'),
    #   )


    # MALE = 'ML'
    # FEMALE = 'FM'

    # SEX = (
    #   (MALE, 'Macho'),
    #   (FEMALE, 'Hembra'),
    #   )

    # LACTATING = 'LC'
    # PREGNANT = 'PG'
    # INCREASE = 'IC'
    # FATTEN = 'FT'

    # PRODUCTIVE = (
    #   (LACTATING, 'Lactante'),
    #   (PREGNANT, 'Gestante'),
    #   (INCREASE, 'Crecimiento'),
    #   (FATTEN, 'Engorda'),
    #   )


    title = models.CharField(max_length=100,)
    description = models.TextField()
    status = models.CharField(max_length=3)
    #user_question =
    #user_response =
    calification = models.IntegerField()

    def __str__(self):
        return '%s' % self.id


class ImageQuestion(models.Model):
    image = models.ImageField(upload_to='questions')
    id_question = models.ForeignKey(Question)

    def __str__(self):
        return '%s' % self.id


class Specie(models.Model):
    race = models.CharField(max_length=3)
    age = models.IntegerField()
    gender = models.CharField(max_length=3)
    weight = models.DecimalField()

    def __str__(self):
        return '%s' % self.id


class Bovine(Specie):
    heart_rate = models.IntegerField()
    respiratory_rate = models.IntegerField()
    temperature = models.DecimalField()
    capilar = models.IntegerField()
    mucosal_color = models.CharField(max_length=30)
    lymph_nodes = models.CharField(max_length=50)
    ruminal = models.CharField(max_length=80)
    body_condition = models.TextField()

    def __str__(self):
        return '%s' % self.id


class Goat(Specie):
    physiological_stage = models.CharField(max_length=30)
    zootechnical = models.CharField(max_length=50)
    production_system = models.CharField(max_length=30)
    heart_rate = models.IntegerField()
    respiratory_rate = models.IntegerField()
    temperature = models.DecimalField()
    capilar = models.IntegerField()
    mucosal_color = models.CharField(max_length=30)
    lymph_nodes = models.CharField(max_length=50)
    ruminal = models.CharField(max_length=80)
    body_condition = models.TextField()
    cough = models.BooleanField()
    def __str__(self):
        return '%s' % self.id


class Rabbit(Specie):
    heart_rate = models.IntegerField()
    respiratory_rate = models.IntegerField()
    temperature = models.DecimalField()
    capilar = models.IntegerField()
    mucosal_color = models.CharField(max_length=30)
    lymph_nodes = models.CharField(max_length=50)
    body_condition = models.TextField()
    dehydration = models.BooleanField()

    def __str__(self):
        return '%s' % self.id


class Cat(Specie):
    heart_rate = models.IntegerField()
    respiratory_rate = models.IntegerField()
    temperature = models.DecimalField()
    capilar = models.IntegerField()
    mucosal_color = models.CharField(max_length=30)
    tusigno_reflex = models.CharField(max_length=30)
    pulse = models.IntegerField()
    injuries = models.CharField(max_length=30)

    def __str__(self):
        return '%s' % self.id


class Ovine(Specie):
    physiological_stage = models.CharField(max_length=30)
    zootechnical = models.CharField(max_length=50)
    production_system = models.CharField(max_length=30)
    heart_rate = models.IntegerField()
    respiratory_rate = models.IntegerField()
    temperature = models.DecimalField()
    mucosal_color = models.CharField(max_length=30)
    lymph_nodes = models.CharField(max_length=50)
    ruminal = models.CharField(max_length=80)
    body_condition = models.TextField()
    cough = models.BooleanField()

    def __str__(self):
        return '%s' % self.id


class Dog(Specie):
    heart_rate = models.IntegerField()
    respiratory_rate = models.IntegerField()
    temperature = models.DecimalField()
    mucosal_color = models.CharField(max_length=30)
    capilar = models.IntegerField()

    def __str__(self):
        return '%s' % self.id


class Porcine(Specie):
    physiological_stage = models.CharField(max_length=30)
    production_system = models.CharField(max_length=30)
    curse = models.CharField(max_length=60)
    respiratory_rate = models.IntegerField()
    temperature = models.DecimalField()
    body_condition = models.TextField()
    attitude = models.TextField()
    color = models.CharField(max_length=30)

    def __str__(self):
        return '%s' % self.id


class Bee(models.Model):
    pass


class Bird(models.Model):
    type_animal = models.CharField(max_length=60)
    zootechnical_purpose = models.CharField(max_length=30)