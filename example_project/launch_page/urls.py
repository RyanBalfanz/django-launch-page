from django.conf.urls import patterns, include, url

from .views import home
from .views import create_inquiry
from .views import create_inquiry_success


urlpatterns = patterns('',
	url(r'^$', home, name='home'),
	url(r'^inquire/$', create_inquiry, name='launch_page_inquire'),
	url(r'^inquire/thanks$', create_inquiry_success, name='launch_page_inquire_thanks'),
)
