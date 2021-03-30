py = python3

format:
	$(py) -m isort .
	$(py) -m black .
