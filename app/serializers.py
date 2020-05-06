# -*- coding: utf-8 -*-
# app/serializers.py

__author__ = 'Flavien-hugs <flavienhgs@pm.me>'
__version__ = '0.0.1'
__copyright__ = '© 2019 unsta'

from rest_framework import serializers

from app.models import Entreprise


class EntrepriseSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Entreprise
        fields = '__all__'
        depth = 1
