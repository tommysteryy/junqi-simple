jun:
	pip install -r requirements.txt
	mkdir -p gamelogs

init:
	pip install -r requirements.txt
	mkdir -p gamelogs

start:
	python start.py

.PHONY: jun