.PHONY: test

test:
	@docker-compose build test
	@docker-compose run --rm test


