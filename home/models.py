from django.db import models

class Question(models.Model):
    BOVINO = 'BV'
    PORCINO  = 'PR'
    EQUINO  = 'EQ'
    OVINO = 'OV'
    GALLUS = 'GL'
    LEPORIDO = 'LP'
    AVE = 'AV'
    CANINO = 'CN'
    FELINO = 'FL'
    SILVESTRE = 'SL'

    SPECIES = (
        (BOVINO, 'Bovino'),
        (PORCINO, 'Porcino'),
        (EQUINO, 'Equino'),
        (OVINO, 'Ovino'),
        (GALLUS, 'Gallus'),
        (LEPORIDO, 'Leporido'),
        (AVE, 'Ave'),
        (CANINO, 'Canino'),
        (FELINO, 'Felino'),
        (SILVESTRE, 'Silvestre'),
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

    PHYSIOLOGICAL= (
        (LACTATING, 'Lactante'),
        (PREGNANT, 'Gestante'),
        (INCREASE, 'Crecimiento'),
    )

    #user = models.ForeignKey(User)
    species = models.CharField(max_length=3, choices=SPECIES, default='')
    question = models.CharField(max_length=100, default='')
    info = models.TextField(default='', blank=True, null=True)
    age = models.models.IntegerField(default=0)
    weight = models.models.IntegerField(default=0)
    gender = models.CharField(max_length=3, choices=SEX, default=MALE)
    Physiological_state = models.CharField(max_length=3, choices=PHYSIOLOGICAL, default=LACTATING)
    reason = models.CharField(max_length=100, default='')
    lpm = models.models.IntegerField(default=0)
    rpm = models.models.IntegerField(default=0)
    temperature = models.models.IntegerField(default=0)
    capillary_filling_time = models.CharField(max_length=100, default='')
    mucous_Coloring = models.CharField(max_length=100, default='')
    lymph_nodes = models.CharField(max_length=100, default='')
    clinic_history = models.TextField(default='', blank=True, null=True)
    date = models.DateTimeField(editable=False, auto_now=True, null=True)
    image = models.ImageField(upload_to='questions', blank=True, null=True)

    def __str__(self):
        return '%s' % self.id
