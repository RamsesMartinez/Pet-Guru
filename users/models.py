from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    DEFAULT_USER = 1

    TEACHER = 'TC'
    STUDENT = 'ST'
    ADMINISTRATOR = 'AD'

    ROL = (
        (TEACHER, 'Profesor'),
        (STUDENT, 'Alumno'),
        (ADMINISTRATOR, 'Administrador'),
    )

    rol = models.CharField(max_length=3, choices=ROL, default='ST')
    speciality = models.CharField(max_length=15)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
