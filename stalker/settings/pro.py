from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ADMINS = (
		('oswaldinho', 'os@fixter.org'), 
	)

ALLOWED_HOSTS = ['oswaldo.actosoftcommunity.com']

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DBNAME'], 
        'USER': os.environ['DBUSER'], 
        'PASSWORD': os.environ['DBPASS'], 
        'HOST': 'localhost'
    }
}

