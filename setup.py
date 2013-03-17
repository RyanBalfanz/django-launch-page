import os
from setuptools import setup

import launch_page as distmeta


README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
	name = 'django-launch-page',
	version=distmeta.__version__,
	packages = ['launch_page'],
	include_package_data = True,
	# license = 'BSD License', # example license
	description=distmeta.__doc__,
	long_description = README,
	url=distmeta.__homepage__,
	author=distmeta.__author__,
	author_email=distmeta.__contact__,
	classifiers = [
		'Environment :: Web Environment',
		'Framework :: Django',
		'Intended Audience :: Developers',
		# 'License :: OSI Approved :: BSD License', # example license
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Programming Language :: Python :: 2.6',
		'Programming Language :: Python :: 2.7',
		'Topic :: Internet :: WWW/HTTP',
		'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
	],
	install_requires=[
		'django>=1.5',
		'South>=0.7.5',
	],
)
