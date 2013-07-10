from .base import *


DEBUG = bool(os.environ.get('DJANGO_DEBUG', 'true'))
TEMPLATE_DEBUG = DEBUG

# DATABASES = {
# 	'default': {
# 		'ENGINE': 'django.db.backends.sqlite3',
# 		'NAME': 'example_project.db',
# 		# The following settings are not used with sqlite3:
# 		'USER': '',
# 		'PASSWORD': '',
# 		'HOST': '',
# 		'PORT': '',
# 	}
# }

DATABASES = {'default': dj_database_url.config(default='sqlite:///example_project.db')}

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '+x0)s27u1p#yq=wfl^g7$l*=sh3rlom920@cp!oo^wj3ouna-4')

MIDDLEWARE_CLASSES += (
	'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INSTALLED_APPS += (
	'debug_toolbar',
)

INTERNAL_IPS = ('127.0.0.1',)
