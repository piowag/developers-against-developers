all: test check_style

test:
	python3 -m unittest discover

check_style: pylint flake8

pylint: install_pylint
	pylint --rcfile=./.pylintrc src/*.py

install_pylint:
	@ if ! hash pylint ; then pip3 install pylint ; fi

flake8: install_flake8
	flake8 --ignore=W191,E117,E501,E128,E722,E123,E101,W191,E117,E501,E128,E722,E123,E101,E305,F401,E302,W605,E302,E305,E302,E302,F403,E225,F405,F405,F405,F405,F405,W293,E251,E251,W293,E231,E231,F405,F405,E231,E231,F405,E303,F405,F405,F405,F405,F405,F405,F405,F405,E231,E111,E306,E306,F405,F405,F405,E231,E201,E231,E231,E231,E201,E231,E231,E231,E201,E231,E231,E111,E111,E111,F405,F405,E111,E111,F405,F405,E111,E111,F405,F405,W292,E302,E305 src/*.py

install_flake8:
	@ if ! hash flake8 ; then pip3 install flake8 ; fi

install_requirements:
	pip3 install -r requirements.txt

.PHONY: test all check_style flake8 pylint install_flake8 install_pylint install_requirements

