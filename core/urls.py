# -*- coding: utf-8 -*-
# core/urls.py

__author__ = 'Flavien-hugs <flavienhgs@pm.me>'
__version__ = '0.0.1'
__copyright__ = '© 2019 unsta'

from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework import routers
from app.views import EntrepriseViewSet

router = routers.DefaultRouter()
router.register(r'api', EntrepriseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('apimin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
