#!/bin/bash

echo "Apply makemigrations"
python manage.py makemigrations

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

echo "Apply data products"
python manage.py loaddata product

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000