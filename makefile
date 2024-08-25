# Makefile

build:
	poetry build

inst:
	poetry install

publish:
	poetry publish --dry-run

lint:
	poetry run flake8 brain_games

package-install:
	pip install whl
	pip install prompt
	pip install asciinema
