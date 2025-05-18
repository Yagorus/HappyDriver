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

# Wait for the database to be ready
echo "Waiting for database to be ready..."
while !</dev/tcp/$DATABASE_HOST/$DATABASE_PORT; do
  sleep 1
  echo "Waiting for database..."
done
echo "Database is ready!"

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

# Import PDD questions
echo "Importing Extended PDD questions..."
if [ -f "/app/extended_pdd_questions.py" ]; then
    echo "Running extended_pdd_questions.py..."
    python /app/extended_pdd_questions.py
    if [ $? -eq 0 ]; then
        echo "Successfully imported Extended PDD questions"
    else
        echo "Failed to import Extended PDD questions, trying standard questions"
        if [ -f "/app/pdd_questions.py" ]; then
            python /app/pdd_questions.py
        fi
    fi
else
    echo "Warning: /app/extended_pdd_questions.py not found. Trying standard questions..."
    if [ -f "/app/pdd_questions.py" ]; then
        python /app/pdd_questions.py
    else
        echo "Warning: /app/pdd_questions.py not found. No questions imported."
    fi
fi

# Import category questions
echo "Importing category questions..."
if [ -f "/app/category_a_questions.py" ]; then
    echo "Importing Category A questions..."
    python /app/category_a_questions.py
fi

if [ -f "/app/category_c_questions.py" ]; then
    echo "Importing Category C questions..."
    python /app/category_c_questions.py
fi 

if [ -f "/app/category_d_questions.py" ]; then
    echo "Importing Category D questions..."
    python /app/category_d_questions.py
    if [ $? -eq 0 ]; then
        echo "Successfully imported Category D questions"
    else
        echo "Failed to import Category D questions"
    fi
fi

if [ -f "/app/category_e_questions.py" ]; then
    echo "Importing Category E questions..."
    python /app/category_e_questions.py
    if [ $? -eq 0 ]; then
        echo "Successfully imported Category E questions"
    else
        echo "Failed to import Category E questions"
    fi
fi

# Import General Traffic Rules questions
echo "Importing General Traffic Rules questions..."
if [ -f "/app/general_questions.py" ]; then
    python /app/general_questions.py
    if [ $? -eq 0 ]; then
        echo "Successfully imported General Traffic Rules questions"
    else
        echo "Failed to import General Traffic Rules questions"
    fi
fi

# Debug database
echo "Running debug_db.py..."
if [ -f "/app/debug_db.py" ]; then
    python /app/debug_db.py
else
    echo "debug_db.py not found. Creating it..."
    echo '
import os
import django
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
django.setup()

from quizzes.models import Quiz, Question, Answer, QuizzesQuestions
from accounts.models import CustomUser

def debug_database():
    print("-" * 50)
    print("DEBUG DATABASE")
    print("-" * 50)
    
    print(f"Quiz count: {Quiz.objects.all().count()}")
    print(f"Question count: {Question.objects.all().count()}")
    print(f"Answer count: {Answer.objects.all().count()}")
    
    try:
        print("Trying to create a simple quiz...")
        
        # Create a superuser if none exists
        if CustomUser.objects.filter(is_superuser=True).count() == 0:
            print("Creating superuser...")
            user = CustomUser.objects.create_superuser("admin", "admin@example.com", "adminpassword")
            print(f"Created superuser: {user.email}")
        
        # Create a quiz
        quiz = Quiz.objects.create(
            title=f"Debug Quiz {Quiz.objects.count() + 1}",
            category="B",
            is_random=False
        )
        print(f"Created quiz: {quiz.title}")
        
        # Create a question
        question = Question.objects.create(
            text="Это отладочный вопрос. Какой ответ правильный?",
            explanation="Это отладочный вопрос."
        )
        print(f"Created question: {question.text}")
        
        # Link question to quiz
        QuizzesQuestions.objects.create(quiz=quiz, question=question)
        print("Linked question to quiz")
        
        # Create answers
        Answer.objects.create(question=question, text="Неправильный ответ", is_correct=False)
        Answer.objects.create(question=question, text="Правильный ответ", is_correct=True)
        Answer.objects.create(question=question, text="Неправильный ответ 2", is_correct=False)
        print("Created answers")
        
        print("Success!")
    except Exception as e:
        print(f"ERROR: {e}")
        print("Exception traceback:")
        import traceback
        traceback.print_exc()
    
    print("-" * 50)

if __name__ == "__main__":
    debug_database()
' > /app/debug_db.py
    python /app/debug_db.py
fi

# Start the server with whitenoise for static files
echo "Starting Gunicorn server..."
gunicorn app.wsgi:application --bind 0.0.0.0:8000
