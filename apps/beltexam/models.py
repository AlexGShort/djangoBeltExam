from __future__ import unicode_literals

from django.db import models
from ..login.models import User

# Create your models here.
class Poke(models.Model):
    poker = models.ForeignKey(User, related_name='poker')
    poked = models.ForeignKey(User, related_name='poked')
