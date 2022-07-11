
export APP_SETTINGS:=config.DevelopmentConfig
export DATABASE_URL:=postgresql://admin:admin@localhost/posts
export FLASK_APP:=project

run:
	py run.py --reload

migrations:
	flask db init

mkmigrations:
	flask db migrate -m "$(name)"

migrate:
	flask db upgrade

history:
	flask db history

tests:
	py tests.py

seeds: 
	py seeds.py

freeze: 
	pip freeze > requirements.txt

help:
	@echo run: flask run
	@echo migrations: flask db init
	@echo mkmigrations: flask db migrate -m "<name>"
	@echo migrate: flask db upgrade
	@echo history: flask db history
	@echo tests: py tests.py
	@echo seeds: py seeds.py
	@echo freeze: pip freeze > requirements.txt
# export DATABASE_URL="sqlite:///posts.db"
