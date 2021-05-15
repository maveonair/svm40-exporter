.PHONY: install dev

install:
	python3 setup.py install --user

dev:
	python3 setup.py develop --user
