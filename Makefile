clean:
	rm -rf ./dist
	rm -rf *.egg-info
	rm -rf ./.tox
	find . -name *.pyc -delete

register:
	python setup.py register

release: test_tox
	python setup.py sdist

test_tox:
	tox --recreate

upload:
	python setup.py upload
