build:
	python setup.py sdist

clean:
	rm -rf ./dist
	rm -rf *.egg-info
	rm -rf ./.coverage
	rm -rf ./.tox
	find . -name *.pyc -delete

register:
	python setup.py register

test: test_basic test_tox

test_basic:
	python example_project/manage.py test

test_tox:
	tox --recreate

upload:
	python setup.py upload
