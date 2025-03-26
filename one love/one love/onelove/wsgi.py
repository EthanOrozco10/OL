"""
WSGI config for onelove project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Set the default settings module for the 'onelove' project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'onelove.settings')


application = get_wsgi_application()
