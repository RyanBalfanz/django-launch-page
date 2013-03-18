import glob
import os

from fabric.api import cd, env, lcd, local, run
from fabric.context_managers import shell_env


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
	lcwd = local("pwd")
	oldPP = os.getenv("PYTHONPATH", "")
	newPP = ":".join([lcwd, oldPP])
	with shell_env(DJANGO_SETTINGS_MODULE="example_project.settings.test", PYTHONPATH=newPP):
		local("python example_project/manage.py test")
