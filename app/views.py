# -*- coding: utf-8 -*-
# apps/views.py

__author__ = 'Flavien-hugs <flavienhgs@pm.me>'
__version__ = '0.0.1'
__copyright__ = '© 2019 unsta'

from rest_framework import viewsets, authentication, permissions

from app.models import Entreprise
from app.serializers import EntrepriseSerializer


class EntrepriseViewSet(viewsets.ModelViewSet):
    queryset = Entreprise.objects.order_by('id')
    serializer_class = EntrepriseSerializer
    authentication_classes = [authentication.SessionAuthentication,
                              authentication.TokenAuthentication,
                              authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
