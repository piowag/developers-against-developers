
pylint: install_pylint
	pylint --rcfile=./.pylintrc src/*

install_pylint:
	@ if ! hash pylint ; then pip3 install pylint ; fi

