# Large Species
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

# Bees tuples

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
  (PRESENT,'Presente'),
  (NOTPRESENT, 'No Presente'),
  (NOTVERIFIED, 'No Verificado'),
  )

BREEDINGCOLOR = 'BC'
PERFORATED = 'PR'
FATTY = 'FT'
APRICOTS = 'APR'
NOTVERIFIED = 'NV'

BREEDING = (
  (BREEDINGCOLOR, 'Larvas de color anormal'),
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
  (NOTVERIFIED, 'NO Verificado')
  )

LARVA = (
  (PRESENT, 'Presente'),
  (NOTPRESENT, 'No Presente'),
  (NOTVERIFIED, 'NO Verificado')
  )

DEADBEES = (
  (PRESENT, 'Presente'),
  (NOTPRESENT, 'No Presente'),
  (NOTVERIFIED, 'NO Verificado')
  )

# Birds tuples

