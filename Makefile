all: lint test

test:
	python -m unittest discover -s tests -vvv

lint:
	flake8 --exclude='\.*',conf.py,'venv/','env/'

ci: lint test
