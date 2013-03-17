import glob
import os

from fabric.api import cd, env, lcd, local, run


def local_build_and_install():
	local("python setup.py sdist")
	with lcd("dist"):
		local("tar -xzvf django-launch-page-*.tar.gz")
		# print "ASDFASDF", local("ls -d -- */")
		print os.getcwd()
		# raise Exception(local("ls -d -- */"))
		# with lcd(local("ls -d -- */")):
		# 	local("python setup.py install")

def local_test():
	local("python example_project/manage.py test")
