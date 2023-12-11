from django.db import models
from applications.users.models import User
from applications.entrada.models import Entry
from .managers import FavoritesManager

#APPS DE TERCEROS
from model_utils.models import TimeStampedModel

# Create your models here.
class Favorites(TimeStampedModel):

    user = models.ForeignKey(User, related_name='user_favorites', on_delete=models.CASCADE)
    entry = models.ForeignKey(Entry, related_name='entry_favorites', on_delete=models.CASCADE)
    objects = FavoritesManager()


    class Meta:
        unique_together = ['user', 'entry']
        verbose_name = 'Entrada Favorita'
        verbose_name_plural = 'Entradas Favoritas'

    def __str__(self):
        return self.entry.title