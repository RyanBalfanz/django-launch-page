clean:
	rm -rf ./dist
	rm -rf *.egg-info
	rm -rf ./.tox
	find . -name *.pyc -delete

register:
	python setup.py register

release: test
	python setup.py sdist

test:
	python example_project/manage.py test

upload:
	python setup.py upload
