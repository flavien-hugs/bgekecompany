# -*- coding: utf-8 -*-
# core/urls.py

__author__ = 'Flavien-hugs <flavienhgs@pm.me>'
__version__ = '0.0.1'
__copyright__ = '© 2019 unsta'

from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static


urlpatterns = [
    path('', include('app.urls', namespace='entreprise')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('apimin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
