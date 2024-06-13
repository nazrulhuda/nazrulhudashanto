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

# Create superuser (replace 'admin' with your desired username)
echo "from django.contrib.auth.models import User; User.objects.create_superuser('naz', 'naz@gmail.com', 'naz108793')" | python manage.py shell

# Optional: You can also create regular users if needed
# echo "from django.contrib.auth.models import User; User.objects.create_user('username', 'email', 'password')" | python manage.py shell