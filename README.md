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

or, bind it to the root domain:

	from launch_page.urls import launch_page_urlpatterns
	urlpatterns += launch_page_urlpatterns


Migrate the application:

	python manage.py migrate launch_page

The use of custom templates is similar to overriding admin templates.

Contributing
------------

Create a new virtualenv:

	mkvirtualenv <env_name>

First, set some environment variables:

	export DJANGO_SETTINGS_MODULE=example_project.settings.local
	export DJANGO_DEBUG=true # Or unset DJANGO_DEBUG to disable
	export DJANGO_SECRET_KEY='your_secret_key'

Add the repository root to your `PYTHONPATH`

	export PYTHONPATH=`pwd`:$PYTHONPATH

or, create a new build and install it to your virtualenv

	make release
	cd dist/
	tar -xzvf django-launch-page-<version>
	cd django-launch-page-<version>/
	python setup.py install

Run the example project with either Foreman or the devserver

	foreman start
	python example_project/manage.py runserver

Testing across multiple Python versions is support with tox. To run the tests with tox:

	make test_tox

[GeoIP]: https://docs.djangoproject.com/en/dev/ref/contrib/gis/geoip/
[tox]: http://tox.readthedocs.org/en/latest/
[Overriding admin templates]: https://docs.djangoproject.com/en/dev/ref/contrib/admin/#overriding-admin-templates
