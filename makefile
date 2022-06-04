run:
	@echo "Running makefile"
	py main.py
install:
	pip install -r requirements.txt
list:
	pip freeze > requirements.txt
dependences:
	pip install virtualenv
init-env:
	.\Scripts\activate.bat
deactivate:
	.\Scripts\deactivate.bat