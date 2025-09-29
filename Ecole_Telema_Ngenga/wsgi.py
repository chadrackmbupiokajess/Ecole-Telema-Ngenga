import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Ecole_Telema_Ngenga.settings')

application = get_wsgi_application()
