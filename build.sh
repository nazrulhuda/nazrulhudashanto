#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies from requirements.txt
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Apply database migrations
python manage.py migrate

# Start the keep_alive management command
python manage.py keep_alive &