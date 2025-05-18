
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

