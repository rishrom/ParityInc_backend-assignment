#!/bin/bash

export POSTGRES_PASSWORD=2YpQCg78gC
export POSTGRES_USER=postgres
export POSTGRES_DB=parity_backend
export POSTGRES_HOST=localhost
export POSTGRES_PORT=54399
export CONTAINER_NAME=parity-backend

echo "Installing requirements via pipenv..."
if ! pipenv --version; then
    echo "  This setup assumed Pipenv is installed on this machine.
  If not, see: https://github.com/pypa/pipenv
"
    exit -1
fi

echo "Pulling Latest PostgreSQL (Docker) Image..."
if ! docker --version; then
    echo "  This setup assumed Docker is installed on this machine.
  If not, see: https://docs.docker.com/v17.09/engine/installation/
"
    exit -1
fi

echo "Checking if PostgreSQL (parity-backend) Docker Image is up and running..."
if ! docker inspect -f '{{.State.Running}}' $CONTAINER_NAME; then
  echo "Starting PostgreSQL (parity-backend) Docker Image"
  docker run --rm --name parity-backend -e POSTGRES_USER=$POSTGRES_USER -e POSTGRES_PASSWORD=$POSTGRES_PASSWORD -e POSTGRES_DB=$POSTGRES_DB -d -p $POSTGRES_PORT:5432 postgres
fi

export LDFLAGS="`pg_config --ldflags`"
pipenv install

echo "Checking for unapplied migrations..."
pipenv run python manage.py makemigrations

echo "Running migrations..."
pipenv run python manage.py migrate

echo "Gathering/building static files..."
pipenv run python manage.py collectstatic

echo "Creating admin user..."
pipenv run python manage.py createsuperuser

sh run.sh
