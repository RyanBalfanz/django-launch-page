import os

from .factory import *


MIDDLEWARE_CLASSES += (
	'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INSTALLED_APPS += (
	'django.contrib.admin',
	'django.contrib.admindocs',
	'south',
	'debug_toolbar',
	'launch_page',
)

INTERNAL_IPS = ('127.0.0.1',)
