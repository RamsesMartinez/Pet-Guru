from django.db import models
from decimal import Decimal, DecimalException
from django.core.validators import MinValueValidator
from . import options
from users.models import User

class Question(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    status = models.CharField(max_length=3, null=True)
    user_question = models.ForeignKey(User, related_name='student_question', default='')
    user_response = models.ForeignKey(User, related_name='teacher_question', default='')
    calification = models.IntegerField(default='1')
    date = models.DateTimeField(editable=False, auto_now=True, null=True)

    def __str__(self):
        return '%s' % self.title


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
    question = models.OneToOneField(Question, default='')
    specie = models.CharField(max_length=10,choices=SPECIES)
    race = models.CharField(max_length=20, null=False)
    age = models.IntegerField(validators=[MinValueValidator(Decimal('0'))])
    gender = models.CharField(max_length=3, choices=SEX, default=MALE)
    weight = models.DecimalField(max_digits=5, decimal_places=3)

    def __str__(self):
        return '%s' % self.id


class Bovine(Specie):
    heart_rate = models.IntegerField()
    respiratory_rate = models.IntegerField()
    temperature = models.DecimalField(max_digits=5, decimal_places=3)
    capilar = models.IntegerField()
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
    heart_rate = models.IntegerField()
    respiratory_rate = models.IntegerField()
    temperature = models.DecimalField(max_digits=5, decimal_places=3)
    capilar = models.IntegerField()
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
    heart_rate = models.IntegerField()
    respiratory_rate = models.IntegerField()
    temperature = models.DecimalField(max_digits=5, decimal_places=3)
    capilar = models.IntegerField()
    mucosal_color = models.CharField(max_length=30, null=True)
    lymph_nodes = models.CharField(max_length=50, null=True)
    body_condition = models.TextField(null=True)
    dehydration = models.CharField(max_length=50, null=True)

    def __str__(self):
        return '%s' % self.id


class Ovine(Specie):
    physiological_stage = models.CharField(max_length=30, null=True)
    zootechnical = models.CharField(max_length=50, null=True)
    production_system = models.CharField(max_length=30, null=True)
    heart_rate = models.IntegerField()
    respiratory_rate = models.IntegerField()
    temperature = models.DecimalField(max_digits=5, decimal_places=3)
    mucosal_color = models.CharField(max_length=30, null=True)
    lymph_nodes = models.CharField(max_length=50, null=True)
    ruminal = models.CharField(max_length=80, null=True)
    body_condition = models.TextField(null=True)

    def __str__(self):
        return '%s' % self.id


class Dog(Specie):
    heart_rate = models.IntegerField()
    respiratory_rate = models.IntegerField()
    temperature = models.DecimalField(max_digits=5, decimal_places=3)
    mucosal_color = models.CharField(max_length=30, null=True)
    capilar = models.IntegerField()
    cough = models.CharField(max_length=80, null=True)
    pulse = models.CharField(max_length=80, null=True)
    skin = models.CharField(max_length=80, null=True)

    def __str__(self): 
        return '%s' % self.id


class Cat(Specie):
    heart_rate = models.IntegerField()
    respiratory_rate = models.IntegerField()
    temperature = models.DecimalField(max_digits=5, decimal_places=3)
    mucosal_color = models.CharField(max_length=30, null=True)
    capilar = models.IntegerField()
    cough = models.CharField(max_length=80, null=True)
    pulse = models.CharField(max_length=80, null=True)
    skin = models.CharField(max_length=80, null=True)

    def __str__(self): 
        return '%s' % self.id


class Porcine(Specie):
    physiological_stage = models.CharField(max_length=30, null=True)
    production_system = models.CharField(max_length=30, null=True)
    curse = models.CharField(max_length=60, null=True)
    heart_rate = models.IntegerField()
    respiratory_rate = models.IntegerField()
    temperature = models.DecimalField(max_digits=5, decimal_places=3)
    body_condition = models.TextField(null=True)
    attitude = models.TextField(null=True)
    color = models.CharField(max_length=30, null=True)

    def __str__(self):
        return '%s' % self.id



class Bee(models.Model):
    RUSTIC = 'RS'
    WILD = 'WL'
    TECHNIFIED = 'TC'
    JUMBO = 'JM'

    COLONY = (
        (RUSTIC, 'Rústica'),
        (WILD, 'Silvestre'),
        (TECHNIFIED, 'Tecnificada Lamgstroth'),
        (JUMBO, 'Tecnificada jumbo'),
    )

    PRESENT = 'PS'
    NOTPRESENT = 'NT'
    NOTVERIFIED = 'NV'

    QUEEN = (
        (PRESENT, 'Presente'),
        (NOTPRESENT, 'No Presente'),
        (NOTVERIFIED, 'No Verificado'),
    )

    LARVACOLOR = 'BC'
    PERFORATED = 'PR'
    FATTY = 'FT'
    APRICOTS = 'APR'
    NOTVERIFIED = 'NV'

    LARVA = (
        (LARVACOLOR, 'Larvas de color anormal'),
        (PERFORATED, 'Perforadas'),
        (FATTY, 'Aspecto grasoso'),
        (APRICOTS, 'Opérculos raídos'),
        (NOTVERIFIED, 'No Verificado'),
    )

    STOMACH = 'ST'
    SLOW = 'SL'
    CHOP = 'CH'
    ALOPECIA = 'LP'
    SHINY = 'SH'
    NOTVERIFIED = 'NV'

    ADULTBEES = (
        (STOMACH, 'Abdomen distendido'),
        (SLOW, 'Lentas'),
        (CHOP, 'Pérdida del instinto de picar'),
        (ALOPECIA, 'Alopécicas'),
        (SHINY, 'Brillosas'),
        (NOTVERIFIED, 'No Verificado'),
    )

    EXCREMENT = (
        (PRESENT, 'Presente'),
        (NOTPRESENT, 'No Presente'),
        (NOTVERIFIED, 'NO Verificado'),
    )

    LARVA = (
        (PRESENT, 'Presente'),
        (NOTPRESENT, 'No Presente'),
        (NOTVERIFIED, 'NO Verificado'),
    )

    DEADBEES = (
        (PRESENT, 'Presente'),
        (NOTPRESENT, 'No Presente'),
        (NOTVERIFIED, 'NO Verificado'),
    )

    question = models.OneToOneField(Question, default='')
    specie = models.CharField(max_length=30)
    colony_type = models.CharField(max_length=3)
    hive_review = models.CharField(max_length=3)
    queen_presence = models.CharField(max_length=3)
    disease_signs = models.CharField(max_length=80)
    breeding = models.CharField(max_length=3)
    adult_bee = models.CharField(max_length=3)
    backstage_bee = models.IntegerField()
    real_cell = models.CharField(max_length=50)
    backstage_breeding = models.IntegerField()
    eggs = models.BooleanField()
    quantity_eggs = models.IntegerField()
    observations = models.TextField()
    stool_spots = models.CharField(max_length=3)
    Piece_larvae = models.CharField(max_length=3)
    dead_bees = models.CharField(max_length=3)
    food_racks = models.CharField(max_length=3)
    number_racks = models.IntegerField()


    def __str__(self):
        return '%s' % self.id


class Bird(models.Model):
    YOUNG = 'YN'
    ADULT = 'SL'

    # Add int fiel to put age in number
    AGE = (
        (YOUNG, 'Joven'),
        (ADULT, 'Adulto'),
    )

    CAGE = 'CG'
    FREE = 'FR'
    HENHOUSE = 'HH'

    CONFINEMENT = (
        (CAGE, 'Jaula'),
        (HENHOUSE, 'Gallinero'),
        (FREE, 'Libre'),
    )

    YES = 'YS'
    NO = 'NO'

    DRINK = (
        (YES, 'Si'),
        (NO, 'No'),
    )

    FOOD = (
        (YES, 'Si'),
        (NO, 'No'),
    )

    LIQUID = 'LQ'
    WHITE = 'WH'
    GREEN = 'GR'
    OTHER = 'TH'
    COMPACT = 'CM'

    DEFECATION = (
        (COMPACT, 'Compactas'),
        (LIQUID, 'Líquidas'),
        (WHITE, 'Blancas'),
        (GREEN, 'Verdes'),
        (OTHER, 'Otros'),
    )

    SCALY = 'SC'
    FLUSHED = 'FL'

    LEGS = (
        (SCALY, 'Escamosas'),
        (FLUSHED, 'Enrojecidas'),
    )

    AQFATTEN = 'FT'
    AQREPRODUCTIVE = 'RP'
    ORNAMENTAL = 'RN'

    AQZOOTECHNICAL = (
        (AQFATTEN, 'Engorda'),
        (AQREPRODUCTIVE, 'Reproductores'),
        (ORNAMENTAL, 'Ornamentales'),
    )

    AQRUSTIC = 'RS'
    AQCEMENT = 'CM'
    AQGEOMEMBRANE = 'GM'
    AQFLOATINGCAGE = 'FC'
    AQOTHER = 'TH'

    POND = (
        (AQRUSTIC, 'Rústico'),
        (AQCEMENT, 'Cemento'),
        (AQGEOMEMBRANE, 'Geomembrana'),
        (AQFLOATINGCAGE, 'Jaula flotante'),
        (AQOTHER, 'Otro'),
    )

    AERATION = (
        (YES, 'Si'),
        (NO, 'No'),
    )

    RECIRCULATION = (
        (YES, 'Si'),
        (NO, 'No'),
    )

    TURBINE = 'TR'
    PROPELLER = 'PR'
    PALETTE = 'PL'
    VERTICAL = 'VR'
    AEREATOROTHER = 'TH'

    AEREATOR = (
        (TURBINE, 'Turbina'),
        (PROPELLER, 'Hélice'),
        (PALETTE, 'Paleta'),
        (VERTICAL, 'Flujo vertical'),
        (AEREATOROTHER, 'Otro'),
    )

    BOTTOM = 'BT'
    MIDDLE = 'MD'
    SURFACE = 'SR'

    COLUMNPOSITION = (
        (BOTTOM, 'Fondo'),
        (MIDDLE, 'Medio'),
        (SURFACE, 'Superficie'),
    )

    NORMAL = 'NR'
    LETHARGIC = 'LT'
    ERRATIC = 'RT'
    SPIRAL = 'SP'
    RUB = 'RB'

    FISHMOVEMENT = (
        (NORMAL, 'Normal'),
        (LETHARGIC, 'Letárgico'),
        (ERRATIC, 'Errático'),
        (SPIRAL, 'En espiral'),
        (RUB, 'Se frotan con la superficie del estanque')
    )

    FISHNORMAL = 'NR'
    FISHDARK = 'DR'

    FISHPOPULATIONCOLOR = (
        (FISHNORMAL, 'Normal'),
        (FISHDARK, 'Obscuro'),
    )

    LACKAPPETITE = (
        (YES, 'Si'),
        (NO, 'No'),
    )

    PELLET = 'PL'
    FLAKE = 'FL'
    LIVE = 'LV'
    FDOTHER = 'TH'

    FOODTYPE = (
        (PELLET, 'Pellet'),
        (FLAKE, 'Hojuela'),
        (LIVE, 'Vivo'),
        (FDOTHER, 'Otro'),
    )

    FISHCOLOR = (
        (FISHNORMAL, 'Normal'),
        (FISHDARK, 'Obscuro'),
    )

    BULGING_BELLY = (
        (YES, 'Si'),
        (NO, 'No'),
    )

    EXOPHTALMIA = (
        (YES, 'Si'),
        (NO, 'No'),
    )

    PETECHIA = (
        (YES, 'Si'),
        (NO, 'No'),
    )

    # Aletas
    FIN = (
        (YES, 'Si'),
        (NO, 'No'),
    )

    ULCERS = (
        (YES, 'Si'),
        (NO, 'No'),
    )

    SORES = (
        (YES, 'Si'),
        (NO, 'No'),
    )

    COTTON_STRUCTURE = (
        (YES, 'Si'),
        (NO, 'No'),
    )

    NECROSIS = (
        (YES, 'Si'),
        (NO, 'No'),
    )

    EYE_OPACITY = (
        (YES, 'Si'),
        (NO, 'No'),
    )
    question = models.OneToOneField(Question, default='')
    type_animal = models.CharField(max_length=60)
    zootechnical_purpose = models.CharField(max_length=30)
    age = models.CharField(max_length=3)
    age_week = models.IntegerField()
    age_month = models.IntegerField()
    place = models.CharField(max_length=60)
    quantity = models.IntegerField()
    coexistence = models.CharField(max_length=30)
    origin_water = models.CharField(max_length=30)
    morbidity = models.CharField(max_length=30)
    mortality = models.CharField(max_length=30)
    date_signs = models.IntegerField()
    water = models.CharField(max_length=3)
    eat = models.CharField(max_length=3)
    vaccine = models.CharField(max_length=30)
    defecation = models.CharField(max_length=3)
    condition_corporal = models.CharField(max_length=30)
    plumage = models.CharField(max_length=50)
    condition_legs = models.CharField(max_length=3)
    breathing_frequency = models.IntegerField()
    dehydration = models.CharField(max_length=3)
    attitude = models.CharField(max_length=80)

    def __str__(self):
        return '%s' % self.id


class Wild(models.Model):
    question = models.OneToOneField(Question, default='')
    specie = models.CharField(max_length=30)
    zootechnical = models.CharField(max_length=50)
    ambiental_condition = models.CharField(max_length=80)
    feeding = models.CharField(max_length=50)
    background = models.CharField(max_length=50)
    evolution_disease = models.CharField(max_length=50)
    heart_rate = models.IntegerField()
    respiratory_rate = models.IntegerField()
    temperature = models.DecimalField(max_digits=5, decimal_places=3)
    capilar = models.IntegerField()
    mucosal_color = models.CharField(max_length=30)
    lymph_nodes = models.CharField(max_length=50)
    ruminal = models.CharField(max_length=80)

    def __str__(self):
        return '%s' % self.id


class Aquatic(models.Model):
    question = models.OneToOneField(Question, default='')
    genetic = models.CharField(max_length=50)
    zootechnical = models.CharField(max_length=50)
    age = models.IntegerField()
    weight = models.IntegerField()
    pond = models.CharField(max_length=3)
    density = models.IntegerField()
    biomass = models.IntegerField()
    aeration = models.CharField(max_length=3)
    aeration_type = models.CharField(max_length=3)
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
    bulging_belly = models.BooleanField()
    exophthalmia = models.BooleanField()
    petechia = models.BooleanField()
    dilated = models.BooleanField()
    ulcers = models.BooleanField()
    skin_sores = models.BooleanField()
    cotton_structures = models.BooleanField()
    necrosis_epidermal_layer = models.BooleanField()
    ocular_opacity = models.BooleanField()

    def __str__(self):
        return '%s' % self.id


class Horse(Specie):
    heart_rate = models.IntegerField()
    respiratory_rate = models.IntegerField()
    temperature = models.DecimalField(max_digits=5, decimal_places=3)
    capilar = models.IntegerField()
    mucosal_color = models.CharField(max_length=30, null=True)
    lymph_nodes = models.CharField(max_length=50, null=True)
    body_condition = models.TextField(null=True)

    def __str__(self):
        return '%s' % self.id