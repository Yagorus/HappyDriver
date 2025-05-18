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
    print("Models imported successfully")
except Exception as e:
    print(f"Error importing models: {e}")
    sys.exit(1)

def create_category_c_data():
    try:
        print("Creating questions for Category C (Грузовые автомобили)...")
        
        # Находим или создаем квиз для категории C
        quiz_c, created = Quiz.objects.get_or_create(
            category="C",
            defaults={
                "title": "Правила дорожнього руху - категорія C",
                "is_random": False
            }
        )
        
        if created:
            print(f"Created quiz C: {quiz_c.title}")
        else:
            print(f"Found existing quiz C: {quiz_c.title}")
            # Очищаем существующие вопросы для квиза
            QuizzesQuestions.objects.filter(quiz=quiz_c).delete()
            print("Cleared existing questions for Category C")
        
        # Создаем словарь для хранения созданных вопросов
        questions_dict = {}
        
        # Вопрос 1
        q = Question.objects.create(
            text="Яка максимальна дозволена маса для вантажного автомобіля категорії C?",
            explanation="Категорія C дозволяє керувати автомобілями, призначеними для перевезення вантажів, дозволена максимальна маса яких перевищує 7500 кг."
        )
        questions_dict["c1"] = q
        QuizzesQuestions.objects.create(quiz=quiz_c, question=q)
        
        Answer.objects.create(question=q, text="3500 кг", is_correct=False)
        Answer.objects.create(question=q, text="5000 кг", is_correct=False)
        Answer.objects.create(question=q, text="7500 кг", is_correct=False)
        Answer.objects.create(question=q, text="Більше 7500 кг", is_correct=True)
        
        # Вопрос 2
        q = Question.objects.create(
            text="Який мінімальний вік необхідний для отримання посвідчення водія категорії C?",
            explanation="Для отримання посвідчення водія категорії C необхідно досягти 18-річного віку."
        )
        questions_dict["c2"] = q
        QuizzesQuestions.objects.create(quiz=quiz_c, question=q)
        
        Answer.objects.create(question=q, text="16 років", is_correct=False)
        Answer.objects.create(question=q, text="17 років", is_correct=False)
        Answer.objects.create(question=q, text="18 років", is_correct=True)
        Answer.objects.create(question=q, text="21 рік", is_correct=False)
        
        # Вопрос 3
        q = Question.objects.create(
            text="Яка максимальна швидкість дозволена для вантажних автомобілів з дозволеною максимальною масою понад 3,5 т на автомагістралях?",
            explanation="На автомагістралях для вантажних автомобілів з дозволеною максимальною масою понад 3,5 т встановлено обмеження швидкості 90 км/год."
        )
        questions_dict["c3"] = q
        QuizzesQuestions.objects.create(quiz=quiz_c, question=q)
        
        Answer.objects.create(question=q, text="70 км/год", is_correct=False)
        Answer.objects.create(question=q, text="80 км/год", is_correct=False)
        Answer.objects.create(question=q, text="90 км/год", is_correct=True)
        Answer.objects.create(question=q, text="110 км/год", is_correct=False)
        
        # Вопрос 4
        q = Question.objects.create(
            text="На яку максимальну відстань може виступати вантаж спереду від вантажного автомобіля?",
            explanation="Вантаж може виступати спереду не більш як на 1 метр від вантажного автомобіля."
        )
        questions_dict["c4"] = q
        QuizzesQuestions.objects.create(quiz=quiz_c, question=q)
        
        Answer.objects.create(question=q, text="0,5 метра", is_correct=False)
        Answer.objects.create(question=q, text="1 метр", is_correct=True)
        Answer.objects.create(question=q, text="1,5 метра", is_correct=False)
        Answer.objects.create(question=q, text="2 метри", is_correct=False)
        
        # Вопрос 5
        q = Question.objects.create(
            text="Яка максимальна дозволена ширина вантажного автомобіля?",
            explanation="Максимальна дозволена ширина вантажного автомобіля становить 2,6 метра."
        )
        questions_dict["c5"] = q
        QuizzesQuestions.objects.create(quiz=quiz_c, question=q)
        
        Answer.objects.create(question=q, text="2,3 метра", is_correct=False)
        Answer.objects.create(question=q, text="2,5 метра", is_correct=False)
        Answer.objects.create(question=q, text="2,6 метра", is_correct=True)
        Answer.objects.create(question=q, text="3 метри", is_correct=False)
        
        # Вопрос 6
        q = Question.objects.create(
            text="Як часто водії вантажних автомобілів повинні проходити медичний огляд?",
            explanation="Водії вантажних автомобілів повинні проходити медичний огляд кожні 2 роки."
        )
        questions_dict["c6"] = q
        QuizzesQuestions.objects.create(quiz=quiz_c, question=q)
        
        Answer.objects.create(question=q, text="Щороку", is_correct=False)
        Answer.objects.create(question=q, text="Кожні 2 роки", is_correct=True)
        Answer.objects.create(question=q, text="Кожні 3 роки", is_correct=False)
        Answer.objects.create(question=q, text="Кожні 5 років", is_correct=False)
        
        # Вопрос 7
        q = Question.objects.create(
            text="Яка максимальна дозволена швидкість для вантажних автомобілів з дозволеною максимальною масою понад 3,5 т в населених пунктах?",
            explanation="В населених пунктах для вантажних автомобілів з дозволеною максимальною масою понад 3,5 т встановлено обмеження швидкості 50 км/год, як і для інших транспортних засобів."
        )
        questions_dict["c7"] = q
        QuizzesQuestions.objects.create(quiz=quiz_c, question=q)
        
        Answer.objects.create(question=q, text="40 км/год", is_correct=False)
        Answer.objects.create(question=q, text="50 км/год", is_correct=True)
        Answer.objects.create(question=q, text="60 км/год", is_correct=False)
        Answer.objects.create(question=q, text="70 км/год", is_correct=False)
        
        # Вопрос 8
        q = Question.objects.create(
            text="Яку мінімальну дистанцію необхідно дотримуватися між вантажними автомобілями на автомагістралях?",
            explanation="На автомагістралях водії вантажних автомобілів з дозволеною максимальною масою понад 3,5 т повинні дотримуватися дистанції не менше 100 метрів."
        )
        questions_dict["c8"] = q
        QuizzesQuestions.objects.create(quiz=quiz_c, question=q)
        
        Answer.objects.create(question=q, text="50 метрів", is_correct=False)
        Answer.objects.create(question=q, text="70 метрів", is_correct=False)
        Answer.objects.create(question=q, text="100 метрів", is_correct=True)
        Answer.objects.create(question=q, text="150 метрів", is_correct=False)
        
        # Вопрос 9
        q = Question.objects.create(
            text="Скільки годин на добу водій вантажного автомобіля може керувати транспортним засобом без перерви?",
            explanation="Водій вантажного автомобіля може керувати транспортним засобом не більше 4,5 годин без перерви."
        )
        questions_dict["c9"] = q
        QuizzesQuestions.objects.create(quiz=quiz_c, question=q)
        
        Answer.objects.create(question=q, text="2 години", is_correct=False)
        Answer.objects.create(question=q, text="3,5 години", is_correct=False)
        Answer.objects.create(question=q, text="4 години", is_correct=False)
        Answer.objects.create(question=q, text="4,5 години", is_correct=True)
        
        # Вопрос 10
        q = Question.objects.create(
            text="Яка мінімальна тривалість перерви для водія вантажного автомобіля після 4,5 годин керування?",
            explanation="Після 4,5 годин керування водій вантажного автомобіля повинен зробити перерву тривалістю не менше 45 хвилин."
        )
        questions_dict["c10"] = q
        QuizzesQuestions.objects.create(quiz=quiz_c, question=q)
        
        Answer.objects.create(question=q, text="15 хвилин", is_correct=False)
        Answer.objects.create(question=q, text="30 хвилин", is_correct=False)
        Answer.objects.create(question=q, text="45 хвилин", is_correct=True)
        Answer.objects.create(question=q, text="60 хвилин", is_correct=False)
        
        # Вопрос 11
        q = Question.objects.create(
            text="Яке розташування на дорозі є правильним для вантажного автомобіля з дозволеною максимальною масою понад 3,5 т на дорогах з трьома і більше смугами руху?",
            explanation="Вантажні автомобілі з дозволеною максимальною масою понад 3,5 т на дорогах з трьома і більше смугами руху повинні рухатися тільки крайньою правою смугою."
        )
        questions_dict["c11"] = q
        QuizzesQuestions.objects.create(quiz=quiz_c, question=q)
        
        Answer.objects.create(question=q, text="Будь-яка смуга руху", is_correct=False)
        Answer.objects.create(question=q, text="Тільки крайня права смуга", is_correct=True)
        Answer.objects.create(question=q, text="Тільки середня смуга", is_correct=False)
        Answer.objects.create(question=q, text="Тільки крайня ліва смуга", is_correct=False)
        
        # Вопрос 12
        q = Question.objects.create(
            text="Як повинен перевозитися вантаж в кузові вантажного автомобіля?",
            explanation="Вантаж повинен бути надійно закріплений, щоб запобігти його падінню, волочінню, травмуванню супроводжуючих осіб і створенню перешкод для руху."
        )
        questions_dict["c12"] = q
        QuizzesQuestions.objects.create(quiz=quiz_c, question=q)
        
        Answer.objects.create(question=q, text="Без обмежень", is_correct=False)
        Answer.objects.create(question=q, text="Надійно закріпленим", is_correct=True)
        Answer.objects.create(question=q, text="Під тентом", is_correct=False)
        Answer.objects.create(question=q, text="З попереджувальними знаками", is_correct=False)
        
        # Вопрос 13
        q = Question.objects.create(
            text="Чи дозволяється перевезення людей у кузові вантажного автомобіля?",
            explanation="Перевезення людей у кузові вантажного автомобіля дозволяється лише за наявності місць для сидіння, встановлених нижче верхнього краю бортів."
        )
        questions_dict["c13"] = q
        QuizzesQuestions.objects.create(quiz=quiz_c, question=q)
        
        Answer.objects.create(question=q, text="Не дозволяється в жодному випадку", is_correct=False)
        Answer.objects.create(question=q, text="Дозволяється без обмежень", is_correct=False)
        Answer.objects.create(question=q, text="Дозволяється лише за наявності місць для сидіння", is_correct=True)
        Answer.objects.create(question=q, text="Дозволяється тільки в присутності супроводжуючої особи", is_correct=False)
        
        # Вопрос 14
        q = Question.objects.create(
            text="Яка максимальна дозволена маса вантажу, що може перевозитися на вантажному автомобілі?",
            explanation="Максимальна дозволена маса вантажу, що може перевозитися на вантажному автомобілі, залежить від його дозволеної максимальної маси."
        )
        questions_dict["c14"] = q
        QuizzesQuestions.objects.create(quiz=quiz_c, question=q)
        
        Answer.objects.create(question=q, text="Не більше 7500 кг", is_correct=False)
        Answer.objects.create(question=q, text="Не більше дозволеної максимальної маси", is_correct=True)
        Answer.objects.create(question=q, text="Більше дозволеної максимальної маси", is_correct=False)
        Answer.objects.create(question=q, text="Більше 7500 кг", is_correct=False)
        
        print(f"Created {len(questions_dict)} questions for Category C")
        return True
    except Exception as e:
        print(f"Error in create_category_c_data: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Running category_c_questions.py script")
    success = create_category_c_data()
    sys.exit(0 if success else 1)
