.PHONY: test deploy-dry-run deploy

test:
	@docker-compose build test
	@docker-compose run --rm test

deploy-dry-run:
	@docker-compose build deploy-dry-run
	@docker-compose run --rm deploy-dry-run

deploy-test:
	@docker-compose build deploy-test
	@docker-compose run --rm deploy-test

deploy-prod:
	@docker-compose build deploy-prod
	@docker-compose run --rm deploy-prod
