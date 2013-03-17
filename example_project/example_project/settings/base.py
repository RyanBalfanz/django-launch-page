import os

from .factory import *


DEBUG = False
TEMPLATE_DEBUG = DEBUG

INSTALLED_APPS += (
	'django.contrib.admin',
	'django.contrib.admindocs',
	'south',
	'launch_page',
)
