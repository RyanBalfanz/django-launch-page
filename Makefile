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
	tox

upload:
	python setup.py upload
