"""
Django settings for favor project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'u&@a!wfxt&##muqzsi!vldt%+_ydp@x9--#!e)2qlb@bnayyj4'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True


TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djangotoolbox',
    'registro_usuarios',
    'votos',
)

MIDDLEWARE_CLASSES = ( 
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'favor.urls'

WSGI_APPLICATION = 'favor.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'testFLs',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '127.0.0.1',# Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '5432',
    },
    'mongodb':{
        'ENGINE': 'django_mongodb_engine',
        'NAME': 'votofls',#os.path.join(BASE_DIR, 'db.sqlite3'),
        'HOST': '127.0.0.1',
        'PORT': '27017',
    }
}



DATABASE_ROUTERS = [ 'votos.routers.RoutersDataBase',]
# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

MEDIA_URL = '/media/'
im = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2] + ['registro_usuarios'])

TEMPLATE_DIRS = (
    os.path.join(im,'templates'),
)
STATIC_URL = '/static/'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#   'django.contrib.staticfiles.finders.DefaultStorageFinder',
)



MEDIA_ROOT = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2] + ['media'])
STATIC_ROOT = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2] + ['content'])

STATICFILES_STORAGE ='django.contrib.staticfiles.storage.CachedStaticFilesStorage'


AUTHENTICATION_BACKENDS = (
    'registro_usuarios.backendsIniciarSesion.EmailOrUsernameModelBackend',
    'django.contrib.auth.backends.ModelBackend',
)


