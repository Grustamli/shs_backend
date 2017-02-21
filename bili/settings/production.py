# -*- coding: utf-8 -*-
from .base import *

DEBUG = get_env_variable("DEBUG")

ALLOWED_HOSTS = get_env_variable("ALLOWED_HOSTS")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_env_variable('DATABASE_NAME'),
        'USER': get_env_variable('DATABASE_USER'),
        'PASSWORD': get_env_variable('DATABASE_PASSWORD'),
        'HOST': '',
        'PORT': '',
    }
}

import dj_database_url
DATABASES["default"]=dj_database_url.config()
# SECURE_PROXY_SSL_HEADER = (‘HTTP_X_FORWARDED_PROTO’, ‘https’)
#
# STATIC_URL = ‘/static/’
# STATIC_ROOT = ‘staticfiles’
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, ‘static’),
# )
