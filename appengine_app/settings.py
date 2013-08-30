# Initialize App Engine and import the default settings (DB backend, etc.).
# If you want to use a different backend you have to remove all occurences
# of "djangoappengine" from this file.
from djangoappengine.settings_base import *

import os
import sys

APP_ROOT = os.path.dirname(os.path.realpath(__file__))

# Activate django-dbindexer for the default database
DATABASES['native'] = DATABASES['default']
DATABASES['default'] = {
    'ENGINE': 'dbindexer', 'TARGET': 'native',
    'DEV_APPSERVER_OPTIONS': {
        'use_sqlite': True,
        'high_replication': True
    }
}
AUTOLOAD_SITECONF = 'indexes'

SECRET_KEY = 'secret_key'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    #'django.contrib.admin',
    'djangotoolbox',
    'autoload',
    'dbindexer',
    'app',
    # djangoappengine should come last, so it can override a few manage.py
    # commands
    'djangoappengine',
)

MIDDLEWARE_CLASSES = (
    # This loads the index definitions, so it has to come first
    'autoload.middleware.AutoloadMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.contrib.messages.context_processors.messages',
)

# This test runner captures stdout and associates tracebacks with their
# corresponding output. Helps a lot with print-debugging.
TEST_RUNNER = 'djangotoolbox.test.CapturingTestSuiteRunner'

LANGUAGE_CODE = 'ru-ua'
USE_I18N = True
USE_L10N = True
TIME_ZONE = 'UTC'
USE_TZ = False
DECIMAL_SEPARATOR = ','
DATE_FORMAT = 'd.m.Y'
DATE_INPUT_FORMATS = ['d.m.Y', ]
DATETIME_FORMAT = 'd.m.Y H:M'
DATETIME_INPUT_FORMATS = ['d.m.Y H:M', ]

ADMIN_MEDIA_PREFIX = '/media/admin/'
TEMPLATE_DIRS = (os.path.join(APP_ROOT, 'templates'),)

ROOT_URLCONF = 'app.urls'

STATIC_URL = '/static/'
MEDIA_URL = '/media/'


PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher',
)


ADMINS_EMAILS = (
    'test@example.com',
)

LOGIN_URL = '/signin/'
LOGOUT_URL = '/signout/'
