
export APP_SETTINGS:=config.DevelopmentConfig
export DATABASE_URL:=postgresql://admin:admin@localhost/posts

run:
	flask run

venv:
	source venv/Scripts/activate

migrations:
	flask db init

mkmigrations:
	flask db migrate -m "Initial migration."

migrate:
	flask db upgrade
	
# export DATABASE_URL="sqlite:///posts.db"