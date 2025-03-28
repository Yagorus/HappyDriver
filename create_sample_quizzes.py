import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()

from quizzes.models import Quiz, Question, Answer, Category, Topic, Paper
from django.contrib.auth.models import User
from django.utils import timezone

def create_sample_data():
    # Check if there are any quizzes
    if Quiz.objects.count() == 0:
        print("No quizzes found. Creating sample data...")
        
        # Create a superuser if none exists
        if User.objects.filter(is_superuser=True).count() == 0:
            User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')
            print("Created superuser: admin/adminpassword")
        
        # Create categories
        road_signs = Category.objects.create(name="Road Signs")
        traffic_rules = Category.objects.create(name="Traffic Rules")
        
        # Create topics
        warning_signs = Topic.objects.create(name="Warning Signs", category=road_signs)
        priority_signs = Topic.objects.create(name="Priority Signs", category=road_signs)
        speed_limits = Topic.objects.create(name="Speed Limits", category=traffic_rules)
        
        # Create papers
        paper_a = Paper.objects.create(name="Paper A")
        paper_b = Paper.objects.create(name="Paper B")
        
        # Create quizzes
        quiz1 = Quiz.objects.create(
            title="Road Signs Quiz",
            description="Test your knowledge of road signs",
            topic=warning_signs,
            paper=paper_a,
            created_at=timezone.now()
        )
        
        quiz2 = Quiz.objects.create(
            title="Traffic Rules Quiz",
            description="Test your knowledge of traffic rules",
            topic=speed_limits,
            paper=paper_b,
            created_at=timezone.now()
        )
        
        # Create questions for quiz1
        q1 = Question.objects.create(
            quiz=quiz1,
            text="What does a triangular sign with a red border usually indicate?",
            image_url="/static/img/logo.jpg"
        )
        
        q2 = Question.objects.create(
            quiz=quiz1,
            text="What does a circular sign with a red border usually indicate?",
            image_url="/static/img/logo.jpg"
        )
        
        # Create answers for q1
        Answer.objects.create(question=q1, text="Warning", is_correct=True)
        Answer.objects.create(question=q1, text="Prohibition", is_correct=False)
        Answer.objects.create(question=q1, text="Information", is_correct=False)
        
        # Create answers for q2
        Answer.objects.create(question=q2, text="Warning", is_correct=False)
        Answer.objects.create(question=q2, text="Prohibition", is_correct=True)
        Answer.objects.create(question=q2, text="Information", is_correct=False)
        
        # Create questions for quiz2
        q3 = Question.objects.create(
            quiz=quiz2,
            text="What is the default speed limit in urban areas?",
            image_url="/static/img/logo.jpg"
        )
        
        q4 = Question.objects.create(
            quiz=quiz2,
            text="When can you exceed the speed limit?",
            image_url="/static/img/logo.jpg"
        )
        
        # Create answers for q3
        Answer.objects.create(question=q3, text="30 km/h", is_correct=False)
        Answer.objects.create(question=q3, text="50 km/h", is_correct=True)
        Answer.objects.create(question=q3, text="70 km/h", is_correct=False)
        
        # Create answers for q4
        Answer.objects.create(question=q4, text="When overtaking", is_correct=False)
        Answer.objects.create(question=q4, text="In an emergency", is_correct=False)
        Answer.objects.create(question=q4, text="Never", is_correct=True)
        
        print(f"Created {Quiz.objects.count()} quizzes")
        print(f"Created {Question.objects.count()} questions")
        print(f"Created {Answer.objects.count()} answers")
    else:
        print(f"Found {Quiz.objects.count()} existing quizzes. Skipping sample data creation.")

if __name__ == "__main__":
    create_sample_data()
