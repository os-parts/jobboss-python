import os

default_app_config = 'jobboss.apps.JobbossConfig'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jobboss.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
