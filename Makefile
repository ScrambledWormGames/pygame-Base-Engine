setup: main.py
	@echo "\n##### Setting up Virtual Environment #####"
	python3 -m venv venv
	@echo "\n##### Enabling environment #####"
	. venv/bin/activate
	@echo "\n##### Downloading requirements #####"
	pip install -r requirements.txt --upgrade pip

run: main.py
	. venv/bin/activate
	python3 main.py

PHONY: clean
clean:
	rm -rf __pycache__
	rm -rf venv
