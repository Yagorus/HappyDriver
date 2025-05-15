#!/bin/bash

# Directly set STATIC_ROOT in settings.py
echo "
# Static files settings
import os
STATIC_ROOT = '/app/staticfiles'
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
" >> app/settings.py

# Update ALLOWED_HOSTS to include the IP address
if grep -q "ALLOWED_HOSTS = " app/settings.py; then
    # If ALLOWED_HOSTS exists, update it to include the IP
    sed -i "s/ALLOWED_HOSTS = \[.*\]/ALLOWED_HOSTS = \['localhost', '127.0.0.1', '147.185.221.26', '*'\]/g" app/settings.py
else
    # If ALLOWED_HOSTS doesn't exist, add it
    echo "ALLOWED_HOSTS = ['localhost', '127.0.0.1', '147.185.221.26', '*']" >> app/settings.py
fi

# Update database settings in settings.py
if grep -q "'HOST': 'localhost'" app/settings.py; then
    sed -i "s/'HOST': 'localhost'/'HOST': '$DATABASE_HOST'/g" app/settings.py
fi
if grep -q "'NAME': 'happy_driver'" app/settings.py; then
    sed -i "s/'NAME': 'happy_driver'/'NAME': '$DATABASE_NAME'/g" app/settings.py
fi
if grep -q "'USER': 'admn'" app/settings.py; then
    sed -i "s/'USER': 'admn'/'USER': '$DATABASE_USER'/g" app/settings.py
fi
if grep -q "'PASSWORD': 'admn'" app/settings.py; then
    sed -i "s/'PASSWORD': 'admn'/'PASSWORD': '$DATABASE_PASSWORD'/g" app/settings.py
fi
if grep -q "'PORT': '5432'" app/settings.py; then
    sed -i "s/'PORT': '5432'/'PORT': '$DATABASE_PORT'/g" app/settings.py
fi

# Create media directory if it doesn't exist
mkdir -p /app/media
mkdir -p /app/staticfiles

# Copy static files to the staticfiles directory
echo "Copying static files..."
cp -r /app/static/* /app/staticfiles/ 2>/dev/null || true

# Skip collectstatic for now
echo "Collecting static files..."
python manage.py collectstatic --noinput --clear

# Create migrations for quizzes app if they don't exist
echo "Checking for quizzes migrations..."
if [ ! -d "/app/quizzes/migrations" ] || [ -z "$(ls -A /app/quizzes/migrations)" ]; then
    echo "Creating migrations for quizzes app..."
    python manage.py makemigrations quizzes
fi

echo "Applying migrations..."
python manage.py migrate

# Fix the home_page view error
if grep -q "latest_quiz.title" /app/quizzes/views.py; then
    sed -i 's/latest_quiz.title/latest_quiz.title if latest_quiz else "No quizzes available"/g' /app/quizzes/views.py
fi

# Start the server with whitenoise for static files
echo "Starting Gunicorn server..."
gunicorn app.wsgi:application --bind 0.0.0.0:8000
