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
    cough = models.CharField(max_length=80, null=True)
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
    specie = models.CharField(max_length=30)
    colony_type = models.CharField(max_length=3)
    hive_review = models.CharField(max_length=3)
    queen_presence = models.CharField(max_length=3)
    disease_signs = models.CharField(max_length=80)
    breeding = models.CharField(max_length=3)
    adult_bee = models.CharField(max_length=3)
    backstage_bee = models.IntegerField(default=0)
    real_cell = models.CharField(max_length=50)
    backstage_breeding = models.IntegerField(default=0)
    eggs = models.BooleanField()
    quantity_eggs = models.IntegerField(default=0)
    observations = models.TextField()
    stool_spots = models.CharField(max_length=3)
    Piece_larvae = models.CharField(max_length=3)
    dead_bees = models.CharField(max_length=3)
    food_racks = models.CharField(max_length=3)
    number_racks = models.IntegerField(default=0)


    def __str__(self):
        return '%s' % self.id


class Bird(models.Model):
    type_animal = models.CharField(max_length=60)
    zootechnical_purpose = models.CharField(max_length=30)
    age = models.CharField(max_length=3)
    age_week = models.IntegerField()
    age_month = models.IntegerField()
    place = models.CharField(max_length=60)
    quantity = models.IntegerField()
    coexistence = models.BooleanField()
    origin_water = models.BooleanField()
    morbidity = models.IntegerField()
    mortality = models.IntegerField()
    date_signs = models.IntegerField()
    water = models.BooleanField()
    eat = models.BooleanField()
    vaccine = models.CharField(max_length=30)
    defecation = models.CharField(max_length=3)
    condition_corporal = models.CharField(max_length=30)
    plumage = models.CharField(max_length=50)
    condition_legs = models.CharField(max_length=3)
    breathing_frequency = models.IntegerField()
    dehydration = models.BooleanField()
    attitude = models.CharField(max_length=80)

    def __str__(self):
        return '%s' % self.id


class wild(models.Model):
    specie = models.CharField(max_length=30)
    zootechnical = models.CharField(max_length=50)
    ambiental_condition = models.CharField(max_length=80)
    feeding = models.CharField(max_length=50)
    background = models.CharField(max_length=50)
    evolution_disease = models.CharField(max_length=50)
    respiratory_rate = models.IntegerField()
    temperature = models.DecimalField(max_digits=5, decimal_places=3)
    capilar = models.IntegerField()
    mucosal_color = models.CharField(max_length=30)
    lymph_nodes = models.CharField(max_length=50)
    ruminal = models.CharField(max_length=80)

    def __str__(self):
        return '%s' % self.id


class aquatic(models.Model):
    zootechnical = models.CharField(max_length=50)
    age = models.IntegerField()
    weight = models.IntegerField()
    pond = models.CharField(max_length=3)
    density = models.IntegerField()
    biomass = models.IntegerField()
    aeration = models.CharField(max_length=3)
    recirculation_water = models.BooleanField()
    change_water = models.PositiveIntegerField()
    date_sowing = models.CharField(max_length=50)
    temperature_6am = models.IntegerField()
    temperature_3pm = models.IntegerField()
    oxygen_6am = models.IntegerField()
    oxygen_3pm = models.IntegerField()
    ph_6am = models.IntegerField()
    ph_3pm = models.IntegerField()
    no2 = models.IntegerField()
    nh4 = models.IntegerField()
    nh3 = models.IntegerField()
    transparency = models.IntegerField()
    mortality = models.IntegerField()
    start_mortality = models.DateField()
    position = models.CharField(max_length=3)
    body_color = models.CharField(max_length=3)
    moves = models.CharField(max_length=3)
    lack_of_appetite = models.BooleanField()
    type_eat = models.CharField(max_length=3)
    eat_for_day = models.CharField(max_length=80)
    coloration = models.CharField(max_length=3)
    Bulging_belly = models.BooleanField()
    Exophthalmia = models.BooleanField()
    Petechia = models.BooleanField()
    Dilated = models.BooleanField()
    Ulcers = models.BooleanField()
    Skin_sores = models.BooleanField()
    Cotton_structures = models.BooleanField()
    Necrosis_epidermal_layer = models.BooleanField()
    Ocular_opacity = models.BooleanField()

    def __str__(self):
        return '%s' % self.id


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