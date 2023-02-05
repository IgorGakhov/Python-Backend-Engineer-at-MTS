# Команды выполняются из директории task3

venv-activate:
	source venv/bin/activate

venv-deactivate:
	deactivate

install:
	pip install -r requirements.txt

start:
	uvicorn src.endpoints:app

freeze:
	pip freeze > requirements.txt
