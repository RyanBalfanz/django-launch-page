import os

from .factory import *


DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Ryan Balfanz', 'ryan@ryanbalfanz.net'),
)

MANAGERS = ADMINS

INSTALLED_APPS += (
	'django.contrib.admin',
	'django.contrib.admindocs',
	'south',
	'launch_page',
)
