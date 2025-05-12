import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()

from quizzes.models import Quiz, Question, Answer, Category, Topic, Paper
from django.contrib.auth.models import User
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
        
        # Create categories if none exist
        if Category.objects.count() == 0:
            print("Creating sample category...")
            category = Category.objects.create(name="Sample Category")
        else:
            category = Category.objects.first()
            print(f"Using existing category: {category.name}")
        
        # Create topics if none exist
        if Topic.objects.count() == 0:
            print("Creating sample topic...")
            topic = Topic.objects.create(name="Sample Topic", category=category)
        else:
            topic = Topic.objects.first()
            print(f"Using existing topic: {topic.name}")
        
        # Create papers if none exist
        if Paper.objects.count() == 0:
            print("Creating sample paper...")
            paper = Paper.objects.create(name="Sample Paper")
        else:
            paper = Paper.objects.first()
            print(f"Using existing paper: {paper.name}")
        
        # Create a quiz
        print("Creating sample quiz...")
        quiz = Quiz.objects.create(
            title="Sample Quiz",
            description="This is a sample quiz for debugging",
            topic=topic,
            paper=paper,
            created_at=timezone.now()
        )
        
        # Create a question
        print("Creating sample question...")
        question = Question.objects.create(
            quiz=quiz,
            text="This is a sample question",
            image_url="/static/img/logo.jpg"
        )
        
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
            print(f"    Description: {quiz.description}")
            print(f"    Topic: {quiz.topic.name if quiz.topic else 'None'}")
            print(f"    Paper: {quiz.paper.name if quiz.paper else 'None'}")
            
            # Check questions
            questions = Question.objects.filter(quiz=quiz)
            print(f"    Questions: {questions.count()}")
            for question in questions:
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
