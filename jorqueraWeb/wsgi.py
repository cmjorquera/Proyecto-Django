"""
WSGI config for jorqueraWeb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
##example for internet
from jorqueraWebApp import app as application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jorqueraWeb.settings')

application = get_wsgi_application()
