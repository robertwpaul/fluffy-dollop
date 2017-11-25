.PHONY: test deploy-dry-run deploy

test:
	@docker-compose build test
	@docker-compose run --rm test

deploy-dry-run:
	@docker-compose build deploy-dry-run
	@docker-compose run --rm deploy-dry-run

deploy:
	@docker-compose build deploy
	@docker-compose run --rm deploy
