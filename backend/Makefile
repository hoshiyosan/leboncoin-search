
services:
	docker-compose up

serve-api:
	FLASK_APP=apartment.api:app .venv/bin/flask run --reload

worker:
	.venv/bin/python -m celery -A apartment.tasks worker --loglevel=INFO --concurrency=10 -n worker1@%h
