# -*- coding: utf-8 -*-
# core/production.py


__author__ = 'Flavien-hugs <contact@unsta.ci>'
__version__ = '0.0.1'
__copyright__ = '© 2019 unsta'

import dj_database_url
from core.settings import *

DEBUG = TEMPLATE_DEBUG = False

# Parse database configuration from $DATABASE_URL
DATABASES['default'] = dj_database_url.config()

# APPLICATION DEFINITION
INSTALLED_APPS += ['whitenoise.runserver_nostatic']

# 'django.middleware.security.SecurityMiddleware',
MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']
#  Add configuration for static files storage using whitenoise

ALLOWED_HOSTS = ["apigbekecompany.herokuapp.com"]
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
)
