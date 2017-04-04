# -*- coding: utf-8 -*-
from .base import *
import dj_database_url

DEBUG = True

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

DATABASES["default"]=dj_database_url.config()


# set S3 as the place to store your files.
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_ACCESS_KEY_ID = get_env_variable('AWS_ACCESS_KEY_ID', '')
AWS_SECRET_ACCESS_KEY = get_env_variable('AWS_SECRET_ACCESS_KEY', '')
AWS_STORAGE_BUCKET_NAME = get_env_variable('AWS_STORAGE_BUCKET_NAME', '')
AWS_QUERYSTRING_AUTH = False #This will make sure that the file URL does not have unnecessary parameters like your access key.#
AWS_S3_CUSTOM_DOMAIN = AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com'
#static media settings
STATIC_URL = 'https://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/'
MEDIA_URL = STATIC_URL + 'media/'
STATICFILES_DIRS = ( os.path.join(BASE_DIR, 'static'), )
STATIC_ROOT = 'staticfiles'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
STATICFILES_FINDERS = (
'django.contrib.staticfiles.finders.FileSystemFinder',
'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)



# SECURE_PROXY_SSL_HEADER = (‘HTTP_X_FORWARDED_PROTO’, ‘https’)
#
# STATIC_URL = ‘/static/’
# STATIC_ROOT = ‘staticfiles’
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, ‘static’),
# )
