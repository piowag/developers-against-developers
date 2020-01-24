
check_style: pylint flake8

pylint: install_pylint
	pylint --rcfile=./.pylintrc src/*

install_pylint:
	@ if ! hash pylint ; then pip3 install pylint ; fi

flake8: install_flake8
	flake8 --ignore=W191,E117,E501,E128,E722,E123,E101 src/*

install_flake8:
	@ if ! hash flake8 ; then pip3 install flake8 ; fi


