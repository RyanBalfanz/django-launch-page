from .base import *


DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': 'example_project.db',
		# The following settings are not used with sqlite3:
		'USER': '',
		'PASSWORD': '',
		'HOST': '',
		'PORT': '',
	}
}

MIDDLEWARE_CLASSES += (
	'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INSTALLED_APPS += (
	'debug_toolbar',
)

INTERNAL_IPS = ('127.0.0.1',)
