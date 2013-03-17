django-launch-page
==================

A launch page for a Django project to collect e-mail addresses and more.

Installing `launch_page` to you Django project will give you a simple teaser page for collecting e-mail addresses, names, and IP addresses.

The IP address can be geolocated with GeoIP. For more information, see the GeoIP documentation.

Installation
------------

Install from PyPI:

	pip install django-launch-page

Add `launch_page` to your `INSTALLED_APPS`:

	INSTALLED_APPS = (
		...
		'launch_page',
	)

Include the `launch_page` URLconf in your project urls.py like this:

	urlpatterns = patterns('',
		...
		url(r'^launch_page/', include('launch_page.urls')),
	)

Migrate the application:

	python manage.py migrate launch_page

Contributing
------------

To install into a local development environment

	make release
	cd dist/django-launch-page-FOO && python setup.py install

Testing across multiple Python versions is support with tox. To run the tests with tox:

	make test_tox

[GeoIP]: https://docs.djangoproject.com/en/dev/ref/contrib/gis/geoip/
[tox]: http://tox.readthedocs.org/en/latest/
