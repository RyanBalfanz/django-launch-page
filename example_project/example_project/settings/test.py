from .base import *


DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {'default': dj_database_url.config(default='sqlite://')} # memory

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '+x0)s27u1p#yq=wfl^g7$l*=sh3rlom920@cp!oo^wj3ouna-4')
