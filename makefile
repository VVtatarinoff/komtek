install:
	poetry install

tests:
	poetry run pytest --verbose


coverage:
	poetry run pytest --cov=references

build:
	poetry build
run:
	poetry run python manage.py runserver

log:
	heroku logs --tail

lint:
	poetry run flake8

translate:
	django-admin compilemessages

command_prompt:
	export PS1="\W ($(git branch 2>/dev/null | grep '^*' | colrm 1 2)) $ "
.PHONY: install  build run tests log lint translate