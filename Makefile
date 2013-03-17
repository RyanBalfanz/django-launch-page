release: test
	python setup.py sdist

test:
	python example_project/manage.py test

clean:
	rm -rf ./dist
	rm -rf *.egg-info
	find . -name *.pyc -delete
