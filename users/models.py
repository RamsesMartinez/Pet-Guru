from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext as _


class User(AbstractUser):
    rol = models.CharField(max_length=3)


    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'