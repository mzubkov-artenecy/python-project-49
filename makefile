# Makefile

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	pip install whl
