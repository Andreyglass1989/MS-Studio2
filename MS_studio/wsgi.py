"""
WSGI config for MS_studio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os,sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MS_studio.settings")
sys.path.append('/root/django/MS_studio')
sys.path.append('/root/django/MS_studio/MS_studio')
application = get_wsgi_application()
