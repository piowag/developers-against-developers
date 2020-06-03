all: test check_style

test:
	python3 -m unittest discover

check_style: pylint flake8

pylint: install_pylint
	pylint --rcfile=./.pylintrc src/*.py

install_pylint:
	@ if ! hash pylint ; then pip3 install pylint ; fi

flake8: install_flake8
	flake8 --ignore=W191,E117,E501,E128,E722,E123,E101 src/*.py

install_flake8:
	@ if ! hash flake8 ; then pip3 install flake8 ; fi

install_requirements:
	pip3 install -r requirements.txt

.PHONY: test all check_style flake8 pylint install_flake8 install_pylint install_requirements

