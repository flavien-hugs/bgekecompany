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

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ALLOWED_HOSTS = ["gbekecompany.herokuapp.com"]

SECURE_HSTS_SECONDS = 15768000  # 6 mois
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_SSL_REDIRECT = True
X_FRAME_OPTIONS = 'DENY'
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_REFERRER_POLICY = 'origin'
SESSION_COOKIE_AGE = 15768000
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_SECURE = True
CACHE_MIDDLEWARE_SECONDS = 5000
CSRF_COOKIE_HTTPONLY = True
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE = 'SameSite'
CSRF_USE_SESSIONS = True
SESSION_COOKIE_NAME = 'api'


