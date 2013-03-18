from django.conf.urls import patterns, include, url

from .views import home
from .views import create_inquiry
from .views import create_inquiry_success


launch_page_urlpatterns = patterns('',
	# url(r'^$', home, name='home'),
	url(r'^inquire$', create_inquiry, name='inquiry_create'),
	url(r'^inquire/thanks$', create_inquiry_success, name='inquiry_create_success'),
)
