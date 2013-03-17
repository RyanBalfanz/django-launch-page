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

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '+x0)s27u1p#yq=wfl^g7$l*=sh3rlom920@cp!oo^wj3ouna-4')
