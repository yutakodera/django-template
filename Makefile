init:
	make build
	make db/flush
	make db/makemigrations
	make db/migrate
	make collectstatic
	make createsuperuser


build:
	docker compose up -d --build

db/flush:
	docker compose run --rm app python manage.py flush --no-input

db/makemigrations:
	docker compose run --rm app python manage.py makemigrations

db/migrate:
	docker compose run --rm app python manage.py migrate

collectstatic:
	docker compose run --rm app python manage.py collectstatic --no-input

createsuperuser:
	docker compose run --rm app python manage.py createsuperuser

app/makeapp:
	docker compose run --rm app python manage.py startapp $(name)

