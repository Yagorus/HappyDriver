import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()

from quizzes.models import Quiz, Question, Answer, QuizzesQuestions
from accounts.models import CustomUser
from django.utils import timezone
import sys

def debug_quizzes():
    print("\n=== DEBUG QUIZZES ===")
    
    # Check if Quiz model exists
    print(f"Quiz model attributes: {[f.name for f in Quiz._meta.get_fields()]}")
    
    # Check if there are any quizzes
    quizzes = Quiz.objects.all()
    print(f"Total quizzes: {quizzes.count()}")
    
    if quizzes.count() == 0:
        print("No quizzes found. Creating a sample quiz...")
        
        # Create a quiz
        print("Creating sample quiz...")
        quiz = Quiz.objects.create(
            title="Sample Quiz",
            category="B",
            is_random=False
        )
        
        # Create a question
        print("Creating sample question...")
        question = Question.objects.create(
            text="This is a sample question",
            explanation="This is an explanation",
        )
        
        # Link the question to the quiz
        QuizzesQuestions.objects.create(quiz=quiz, question=question)
        
        # Create answers
        print("Creating sample answers...")
        Answer.objects.create(question=question, text="Answer 1", is_correct=True)
        Answer.objects.create(question=question, text="Answer 2", is_correct=False)
        Answer.objects.create(question=question, text="Answer 3", is_correct=False)
        
        print("Sample quiz created successfully!")
    else:
        print("Existing quizzes:")
        for quiz in quizzes:
            print(f"  - {quiz.id}: {quiz.title} (created: {quiz.created_at})")
            print(f"    Category: {quiz.category}")
            print(f"    Is Random: {quiz.is_random}")
            
            # Check questions
            quiz_questions = QuizzesQuestions.objects.filter(quiz=quiz)
            print(f"    Questions: {quiz_questions.count()}")
            for quiz_question in quiz_questions:
                question = quiz_question.question
                print(f"      - {question.id}: {question.text}")
                
                # Check answers
                answers = Answer.objects.filter(question=question)
                print(f"        Answers: {answers.count()}")
                for answer in answers:
                    print(f"          - {answer.id}: {answer.text} (correct: {answer.is_correct})")
    
    # Debug the home_page view
    print("\n=== DEBUG HOME PAGE VIEW ===")
    try:
        from quizzes.views import home_page
        print("home_page view function exists")
        
        # Check what latest_quiz would be
        latest_quiz = Quiz.objects.order_by('-created_at').first()
        print(f"Latest quiz: {latest_quiz}")
        if latest_quiz:
            print(f"  - Title: {latest_quiz.title}")
            print(f"  - Created at: {latest_quiz.created_at}")
        else:
            print("No latest quiz found")
    except ImportError:
        print("Could not import home_page view")
    
    # Debug the template
    print("\n=== DEBUG TEMPLATE ===")
    try:
        from django.template.loader import get_template
        template = get_template('home.html')
        print("home.html template exists")
    except Exception as e:
        print(f"Error loading template: {e}")
    
    print("\n=== END DEBUG ===")

if __name__ == "__main__":
    debug_quizzes()
