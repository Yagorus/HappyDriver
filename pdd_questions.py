import os
import django
import random
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

try:
    django.setup()
    print("Django setup successful")
except Exception as e:
    print(f"Error during Django setup: {e}")
    sys.exit(1)

try:
    from quizzes.models import Quiz, Question, Answer, QuizzesQuestions
    from accounts.models import CustomUser
    from django.utils import timezone
    print("Models imported successfully")
except Exception as e:
    print(f"Error importing models: {e}")
    sys.exit(1)

def create_pdd_data():
    try:
        # Check if there are any quizzes
        quiz_count = Quiz.objects.count()
        question_count = Question.objects.count()
        print(f"Current quiz count: {quiz_count}")
        print(f"Current question count: {question_count}")
        
        if question_count == 0:
            print("No questions found. Creating PDD test data...")
            
            # Delete existing quizzes if they have no questions
            if quiz_count > 0:
                print("Removing existing quizzes without questions...")
                Quiz.objects.all().delete()
                print("Existing quizzes deleted.")
            
            # Create a superuser if none exists
            if CustomUser.objects.filter(is_superuser=True).count() == 0:
                CustomUser.objects.create_superuser(email='admin@example.com', password='adminpassword')
                print("Created superuser: admin@example.com")
            
            # Create quizzes for different categories
            quiz_a = Quiz.objects.create(
                title="Правила дорожнього руху - категорія A",
                category="A",
                is_random=False
            )
            print(f"Created quiz A: {quiz_a.title}")
            
            quiz_b = Quiz.objects.create(
                title="Правила дорожнього руху - категорія B",
                category="B",
                is_random=False
            )
            print(f"Created quiz B: {quiz_b.title}")
            
            quiz_c = Quiz.objects.create(
                title="Правила дорожнього руху - категорія C",
                category="C",
                is_random=False
            )

            quiz_common = Quiz.objects.create(
                title="Загальні правила дорожнього руху",
                category="ALL",
                is_random=False
            )
            
            # Create questions for category A (мотоциклы)
            q1 = Question.objects.create(
                text="Яка максимальна швидкість дозволена для мотоциклів на автомагістралях в Україні?",
                explanation="Згідно з ПДР України, на автомагістралях для мотоциклів встановлено обмеження швидкості 130 км/год."
            )
            
            q2 = Question.objects.create(
                text="Чи може мотоцикліст їхати між рядами транспортних засобів, що стоять або рухаються в заторі?",
                explanation="Рух між рядами транспортних засобів заборонений згідно з ПДР."
            )
            
            q3 = Question.objects.create(
                text="З якого віку можна керувати мотоциклом (категорія A) в Україні?",
                explanation="Посвідчення водія категорії А можна отримати з 16 років."
            )
            
            # Link questions to quiz_a
            QuizzesQuestions.objects.create(quiz=quiz_a, question=q1)
            QuizzesQuestions.objects.create(quiz=quiz_a, question=q2)
            QuizzesQuestions.objects.create(quiz=quiz_a, question=q3)
            
            # Add to common quiz as well
            QuizzesQuestions.objects.create(quiz=quiz_common, question=q1)
            
            # Create answers for q1
            Answer.objects.create(question=q1, text="90 км/год", is_correct=False)
            Answer.objects.create(question=q1, text="110 км/год", is_correct=False)
            Answer.objects.create(question=q1, text="130 км/год", is_correct=True)
            Answer.objects.create(question=q1, text="150 км/год", is_correct=False)
            
            # Create answers for q2
            Answer.objects.create(question=q2, text="Так, але тільки при швидкості до 20 км/год", is_correct=False)
            Answer.objects.create(question=q2, text="Так, це дозволено в будь-якому випадку", is_correct=False)
            Answer.objects.create(question=q2, text="Ні, це заборонено", is_correct=True)
            
            # Create answers for q3
            Answer.objects.create(question=q3, text="14 років", is_correct=False)
            Answer.objects.create(question=q3, text="16 років", is_correct=True)
            Answer.objects.create(question=q3, text="18 років", is_correct=False)
            Answer.objects.create(question=q3, text="21 рік", is_correct=False)
            
            # Create questions for category B (легковые авто)
            q4 = Question.objects.create(
                text="На якій відстані від пішохідного переходу заборонена зупинка транспортних засобів?",
                explanation="Згідно з ПДР, зупинка заборонена ближче ніж за 50 м до пішохідного переходу."
            )
            
            q5 = Question.objects.create(
                text="Яка максимальна швидкість руху в населених пунктах України?",
                explanation="Згідно з ПДР, в населених пунктах дозволяється рух зі швидкістю не більше 50 км/год."
            )
            
            q6 = Question.objects.create(
                text="Чи можна використовувати телефон під час керування автомобілем?",
                explanation="Водій може розмовляти по телефону тільки за допомогою спеціальних пристроїв (гарнітури), які дозволяють керувати без допомоги рук."
            )
            
            # Link questions to quiz_b
            QuizzesQuestions.objects.create(quiz=quiz_b, question=q4)
            QuizzesQuestions.objects.create(quiz=quiz_b, question=q5)
            QuizzesQuestions.objects.create(quiz=quiz_b, question=q6)
            
            # Add to common quiz as well
            QuizzesQuestions.objects.create(quiz=quiz_common, question=q5)
            QuizzesQuestions.objects.create(quiz=quiz_common, question=q6)
            
            # Create answers for q4
            Answer.objects.create(question=q4, text="10 м", is_correct=False)
            Answer.objects.create(question=q4, text="30 м", is_correct=False)
            Answer.objects.create(question=q4, text="50 м", is_correct=True)
            Answer.objects.create(question=q4, text="100 м", is_correct=False)
            
            # Create answers for q5
            Answer.objects.create(question=q5, text="50 км/год", is_correct=True)
            Answer.objects.create(question=q5, text="60 км/год", is_correct=False)
            Answer.objects.create(question=q5, text="70 км/год", is_correct=False)
            Answer.objects.create(question=q5, text="90 км/год", is_correct=False)
            
            # Create answers for q6
            Answer.objects.create(question=q6, text="Так, у будь-якому випадку", is_correct=False)
            Answer.objects.create(question=q6, text="Ні, це заборонено у будь-якому випадку", is_correct=False)
            Answer.objects.create(question=q6, text="Так, але тільки за допомогою гарнітури", is_correct=True)
            Answer.objects.create(question=q6, text="Так, але тільки під час зупинки", is_correct=False)
            
            # Create questions for category C (грузовые авто)
            q7 = Question.objects.create(
                text="Яка максимальна дозволена маса для вантажного автомобіля категорії C?",
                explanation="Категорія C дозволяє керувати автомобілями, призначеними для перевезення вантажів, дозволена максимальна маса яких перевищує 7500 кг."
            )
            
            q8 = Question.objects.create(
                text="Який мінімальний вік необхідний для отримання посвідчення водія категорії C?",
                explanation="Для отримання посвідчення водія категорії C необхідно досягти 18-річного віку."
            )
            
            # Link questions to quiz_c
            QuizzesQuestions.objects.create(quiz=quiz_c, question=q7)
            QuizzesQuestions.objects.create(quiz=quiz_c, question=q8)
            
            # Add to common quiz as well
            QuizzesQuestions.objects.create(quiz=quiz_common, question=q7)
            
            # Create answers for q7
            Answer.objects.create(question=q7, text="3500 кг", is_correct=False)
            Answer.objects.create(question=q7, text="5000 кг", is_correct=False)
            Answer.objects.create(question=q7, text="7500 кг", is_correct=False)
            Answer.objects.create(question=q7, text="Більше 7500 кг", is_correct=True)
            
            # Create answers for q8
            Answer.objects.create(question=q8, text="16 років", is_correct=False)
            Answer.objects.create(question=q8, text="17 років", is_correct=False)
            Answer.objects.create(question=q8, text="18 років", is_correct=True)
            Answer.objects.create(question=q8, text="21 рік", is_correct=False)
            
            # Create common questions
            q9 = Question.objects.create(
                text="Коли необхідно увімкнути ближнє світло фар у світлу пору доби?",
                explanation="Згідно з ПДР, водії мають вмикати ближнє світло фар або денні ходові вогні в світлу пору доби на всіх транспортних засобах."
            )
            
            q10 = Question.objects.create(
                text="Яким учасникам дорожнього руху водій повинен надати перевагу під час руху на регульованому перехресті?",
                explanation="Водій повинен надати перевагу пішоходам, які переходять дорогу, на яку він повертає, та велосипедистам, які рухаються по велосипедній доріжці, що перетинає його шлях."
            )
            
            # Link questions to common quiz
            QuizzesQuestions.objects.create(quiz=quiz_common, question=q9)
            QuizzesQuestions.objects.create(quiz=quiz_common, question=q10)
            
            # Create answers for q9
            Answer.objects.create(question=q9, text="Тільки в умовах недостатньої видимості", is_correct=False)
            Answer.objects.create(question=q9, text="У будь-який час доби", is_correct=True)
            Answer.objects.create(question=q9, text="Тільки в тунелях", is_correct=False)
            Answer.objects.create(question=q9, text="Тільки під час дощу", is_correct=False)
            
            # Create answers for q10
            Answer.objects.create(question=q10, text="Тільки пішоходам", is_correct=False)
            Answer.objects.create(question=q10, text="Тільки велосипедистам", is_correct=False)
            Answer.objects.create(question=q10, text="Пішоходам і велосипедистам", is_correct=True)
            Answer.objects.create(question=q10, text="Нікому, регульоване перехрестя передбачає рух тільки за сигналами світлофора", is_correct=False)
            
            # Create a quiz with random questions
            random_quiz = Quiz.objects.create(
                title="Випадковий тест ПДР",
                category="ALL",
                is_random=True
            )
            
            # Get all questions and add random 5 to the random quiz
            all_questions = Question.objects.all()
            random_questions = random.sample(list(all_questions), min(5, all_questions.count()))
            for question in random_questions:
                QuizzesQuestions.objects.create(quiz=random_quiz, question=question)
            
            print(f"Created {Quiz.objects.count()} quizzes")
            print(f"Created {Question.objects.count()} questions")
            print(f"Created {Answer.objects.count()} answers")
            return True
        else:
            print(f"Found {question_count} existing questions. Skipping data creation.")
            return False
    except Exception as e:
        print(f"Error in create_pdd_data: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Running pdd_questions.py script")
    success = create_pdd_data()
    sys.exit(0 if success else 1)
