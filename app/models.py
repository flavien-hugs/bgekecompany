# -*- coding: utf-8 -*-
# app/models.py

__author__ = 'Flavien-hugs <flavienhgs@pm.me>'
__version__ = '0.0.1'
__copyright__ = '© 2019 unsta'

from django.db import models


class Entreprise(models.Model):
    name = models.CharField("Nom de l'entreprise", max_length=30, unique=True)
    director = models.CharField("Directeur Général", default='Mr/Mme', max_length=30)
    domaine = models.CharField("Domaine d'activité", max_length=50)
    email = models.EmailField('Adresse email', unique=True, blank=True)
    contact = models.CharField('Contact', default='+225 00 00 00 00', max_length=50)
    link = models.URLField('Site internet', default='https://', blank=True)
    location = models.CharField('Lieu', max_length=50)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
