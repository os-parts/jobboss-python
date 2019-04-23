import os
import sys

# database authentication from environment
DB_HOST = os.environ.get('JOBBOSS_DB_HOST')
DB_NAME = os.environ.get('JOBBOSS_DB_NAME')
DB_USERNAME = os.environ.get('JOBBOSS_DB_USERNAME', 'sa')
DB_PASSWORD = os.environ.get('JOBBOSS_DB_PASSWORD')

# Django boilerplate
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INSTALLED_APPS = ['jobboss',]
MIDDLEWARE = []
WSGI_APPLICATION = 'jobboss.application'

IS_TEST = 'test' in sys.argv

# set up database for test or production
if IS_TEST:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3'
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'sql_server.pyodbc',
            'HOST': DB_HOST,
            'NAME': DB_NAME,
            'USER': DB_USERNAME,
            'PASSWORD': DB_PASSWORD
        }
    }

SECRET_KEY = '...'
