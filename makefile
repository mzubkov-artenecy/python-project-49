# Makefile

build:
	poetry build

publish:
	poetry publish --dry-run

lint:
	poetry run flake8 brain_games

package-install:
	pip install whl
