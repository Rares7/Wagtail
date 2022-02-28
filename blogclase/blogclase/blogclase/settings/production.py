#from blogclase.blogclase.blogclase.settings.dev import ALLOWED_HOSTS
from .base import *

DEBUG = False

SECRET_KEY = 'django-insecure-u@lu-10&okux92iolx-tgo))qdnug1!$7zikwn*y*nl%(9g)#A'

ALLOWED_HOSTS = ['*']

import os
DATABASES = {
  "default": {
    "ENGINE": "django.db.backends.postgresql",
    "NAME": "datosrares",
    "USER": "rares",
    "PASSWORD": "rares",
    "HOST": "localhost",
    "PORT": "5432",
  }
}

try:
    from .local import *
except ImportError:
    pass
