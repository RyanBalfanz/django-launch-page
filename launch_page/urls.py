from django.conf.urls import patterns, include, url

from .views import HomeView
from .views import InquiryCreate
from .views import InquiryCreateSuccess


urlpatterns = patterns('',
	url(r'^$', HomeView.as_view(), name='inquiry_home'),
	url(r'^inquire/$', InquiryCreate.as_view(), name='inquiry_create'),
	url(r'^inquire/thanks/$', InquiryCreateSuccess.as_view(), name='inquiry_create_success'),
)
