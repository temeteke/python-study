.PHONY: build run test
build:
	docker-compose build

run:
	docker-compose run --rm app python -m mypackage

test:
	docker-compose run --rm app python -m pytest
