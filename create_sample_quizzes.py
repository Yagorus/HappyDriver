import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()

from quizzes.models import Quiz, Question, Answer, QuizzesQuestions
from accounts.models import CustomUser
from django.utils import timezone

def create_sample_data():
    # Check if there are any quizzes
    if Quiz.objects.count() == 0:
        print("No quizzes found. Creating sample data...")
        
        # Create a superuser if none exists
        if CustomUser.objects.filter(is_superuser=True).count() == 0:
            CustomUser.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')
            print("Created superuser: admin/adminpassword")
        
        # Create quizzes
        quiz1 = Quiz.objects.create(
            title="Road Signs Quiz",
            category="B",
            is_random=False
        )
        
        quiz2 = Quiz.objects.create(
            title="Traffic Rules Quiz",
            category="B",
            is_random=False
        )
        
        # Create questions for quiz1
        q1 = Question.objects.create(
            text="What does a triangular sign with a red border usually indicate?"
        )
        
        q2 = Question.objects.create(
            text="What does a circular sign with a red border usually indicate?"
        )
        
        # Link questions to quiz1
        QuizzesQuestions.objects.create(quiz=quiz1, question=q1)
        QuizzesQuestions.objects.create(quiz=quiz1, question=q2)
        
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
            text="What is the default speed limit in urban areas?"
        )
        
        q4 = Question.objects.create(
            text="When can you exceed the speed limit?"
        )
        
        # Link questions to quiz2
        QuizzesQuestions.objects.create(quiz=quiz2, question=q3)
        QuizzesQuestions.objects.create(quiz=quiz2, question=q4)
        
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
