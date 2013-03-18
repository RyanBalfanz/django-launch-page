import dj_database_url

from .base import *


DEBUG = bool(os.environ.get('DJANGO_DEBUG', 'true'))
TEMPLATE_DEBUG = DEBUG

DATABASES['default'] =  dj_database_url.config()

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '')

MIDDLEWARE_CLASSES += (
	'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INSTALLED_APPS += (
	'debug_toolbar',
)

INTERNAL_IPS = ('127.0.0.1',)

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
