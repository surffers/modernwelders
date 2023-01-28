from .base import *

INSTALLED_APPS += ['debug_toolbar', ]

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': env('DB_ENGINE'),
        'NAME': env('DB_NAME'),
    }
}

#debag_toolbar
INTERNAL_IPS = [
    '127.0.0.1',
]

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'