#!/bin/bash

# Apply database migrations
echo "Apply database migrations"
#python manage.py makemigrations
python manage.py migrate

# Start server
echo "Starting server"
gunicorn task_tracker.wsgi -b 0.0.0.0:8000