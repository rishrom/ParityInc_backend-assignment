#!/bin/bash

export POSTGRES_PASSWORD=2YpQCg78gC
export POSTGRES_USER=postgres
export POSTGRES_DB=parity_backend
export POSTGRES_HOST=localhost
export POSTGRES_PORT=54399

echo "Running localserver at http://127.0.0.1:8008..."
pipenv run python manage.py runserver 127.0.0.1:8008
