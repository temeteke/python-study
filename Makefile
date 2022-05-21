.PHONY: build up down clean run run-local run-docker run-docker-run test test-local test-docker test-docker-run test-docker-exec
build:
	docker-compose build

up:
	docker-compose up

down:
	docker-compose down

clean:
	docker-compose down --rmi all --volumes --remove-orphans

run: run-docker

run-local:
	python -m mypackage

run-docker: run-docker-run

run-docker-run:
	docker-compose run --rm app python -m mypackage

run-docker-exec:
	docker-compose exec app python -m mypackage

test: test-docker

test-local:
	python -m pytest

test-docker: test-docker-run

test-docker-run:
	docker-compose run --rm app python -m pytest

test-docker-exec:
	docker-compose exec app python -m pytest
