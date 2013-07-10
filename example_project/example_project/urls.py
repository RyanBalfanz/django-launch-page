from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
	url(r'', include('launch_page.urls')),
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
	from django.contrib.staticfiles.urls import staticfiles_urlpatterns
	urlpatterns += staticfiles_urlpatterns()
