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

def create_category_e_data():
    try:
        print("Creating questions for Category E (Прицепы)...")
        
        # Находим или создаем квиз для категории E
        quiz_e, created = Quiz.objects.get_or_create(
            category="E",
            defaults={
                "title": "Правила дорожнього руху - категорія E",
                "is_random": False
            }
        )
        
        if created:
            print(f"Created quiz E: {quiz_e.title}")
        else:
            print(f"Found existing quiz E: {quiz_e.title}")
            # Очищаем существующие вопросы для квиза
            QuizzesQuestions.objects.filter(quiz=quiz_e).delete()
            print("Cleared existing questions for Category E")
        
        # Создаем словарь для хранения созданных вопросов
        questions_dict = {}
        
        # Вопрос 1
        q = Question.objects.create(
            text="Яка максимальна дозволена маса для причепа категорії E?",
            explanation="Категорія E дозволяє керувати автопоїздами з причепом, дозволена максимальна маса якого перевищує 750 кг."
        )
        questions_dict["e1"] = q
        QuizzesQuestions.objects.create(quiz=quiz_e, question=q)
        
        Answer.objects.create(question=q, text="350 кг", is_correct=False)
        Answer.objects.create(question=q, text="500 кг", is_correct=False)
        Answer.objects.create(question=q, text="750 кг", is_correct=False)
        Answer.objects.create(question=q, text="Більше 750 кг", is_correct=True)
        
        # Вопрос 2
        q = Question.objects.create(
            text="Який мінімальний вік необхідний для отримання посвідчення водія категорії E?",
            explanation="Для отримання посвідчення водія категорії E необхідно досягти 19-річного віку."
        )
        questions_dict["e2"] = q
        QuizzesQuestions.objects.create(quiz=quiz_e, question=q)
        
        Answer.objects.create(question=q, text="18 років", is_correct=False)
        Answer.objects.create(question=q, text="19 років", is_correct=True)
        Answer.objects.create(question=q, text="21 рік", is_correct=False)
        Answer.objects.create(question=q, text="24 роки", is_correct=False)
        
        # Вопрос 3
        q = Question.objects.create(
            text="Яка максимальна дозволена швидкість руху для автомобілів з причепами на автомагістралях?",
            explanation="На автомагістралях для автомобілів з причепами встановлено обмеження швидкості 80 км/год."
        )
        questions_dict["e3"] = q
        QuizzesQuestions.objects.create(quiz=quiz_e, question=q)
        
        Answer.objects.create(question=q, text="70 км/год", is_correct=False)
        Answer.objects.create(question=q, text="80 км/год", is_correct=True)
        Answer.objects.create(question=q, text="90 км/год", is_correct=False)
        Answer.objects.create(question=q, text="110 км/год", is_correct=False)
        
        # Вопрос 4
        q = Question.objects.create(
            text="Чи дозволяється буксирування автомобілем з причепом?",
            explanation="Буксирування автомобілем з причепом заборонено."
        )
        questions_dict["e4"] = q
        QuizzesQuestions.objects.create(quiz=quiz_e, question=q)
        
        Answer.objects.create(question=q, text="Так, це дозволено", is_correct=False)
        Answer.objects.create(question=q, text="Ні, це заборонено", is_correct=True)
        Answer.objects.create(question=q, text="Дозволено тільки в населених пунктах", is_correct=False)
        Answer.objects.create(question=q, text="Дозволено тільки за межами населених пунктів", is_correct=False)
        
        # Вопрос 5
        q = Question.objects.create(
            text="Яка максимальна дозволена швидкість руху для автомобілів з причепами в населених пунктах?",
            explanation="В населених пунктах для автомобілів з причепами встановлено обмеження швидкості 50 км/год."
        )
        questions_dict["e5"] = q
        QuizzesQuestions.objects.create(quiz=quiz_e, question=q)
        
        Answer.objects.create(question=q, text="40 км/год", is_correct=False)
        Answer.objects.create(question=q, text="50 км/год", is_correct=True)
        Answer.objects.create(question=q, text="60 км/год", is_correct=False)
        Answer.objects.create(question=q, text="70 км/год", is_correct=False)
        
        # Вопрос 6
        q = Question.objects.create(
            text="Що потрібно перевірити перед початком руху з причепом?",
            explanation="Перед початком руху з причепом потрібно перевірити справність зчіпного пристрою, правильність приєднання, роботу світлових приладів."
        )
        questions_dict["e6"] = q
        QuizzesQuestions.objects.create(quiz=quiz_e, question=q)
        
        Answer.objects.create(question=q, text="Тільки роботу світлових приладів", is_correct=False)
        Answer.objects.create(question=q, text="Тільки справність зчіпного пристрою", is_correct=False)
        Answer.objects.create(question=q, text="Справність зчіпного пристрою, правильність приєднання, роботу світлових приладів", is_correct=True)
        Answer.objects.create(question=q, text="Тільки тиск у шинах", is_correct=False)
        
        # Вопрос 7
        q = Question.objects.create(
            text="Хто має право керувати автомобілем з причепом, якщо повна маса причепа перевищує 750 кг?",
            explanation="Керувати автомобілем з причепом, якщо повна маса причепа перевищує 750 кг, має право водій з категорією E."
        )
        questions_dict["e7"] = q
        QuizzesQuestions.objects.create(quiz=quiz_e, question=q)
        
        Answer.objects.create(question=q, text="Водій з категорією B", is_correct=False)
        Answer.objects.create(question=q, text="Водій з категорією C", is_correct=False)
        Answer.objects.create(question=q, text="Водій з категорією D", is_correct=False)
        Answer.objects.create(question=q, text="Водій з категорією E", is_correct=True)
        
        # Вопрос 8
        q = Question.objects.create(
            text="Яка максимальна дозволена довжина автопоїзда (тягач з причепом)?",
            explanation="Максимальна дозволена довжина автопоїзда (тягач з причепом) становить 22 метри."
        )
        questions_dict["e8"] = q
        QuizzesQuestions.objects.create(quiz=quiz_e, question=q)
        
        Answer.objects.create(question=q, text="18 метрів", is_correct=False)
        Answer.objects.create(question=q, text="20 метрів", is_correct=False)
        Answer.objects.create(question=q, text="22 метри", is_correct=True)
        Answer.objects.create(question=q, text="24 метри", is_correct=False)
        
        # Вопрос 9
        q = Question.objects.create(
            text="Чи дозволяється перевезення пасажирів у причепі?",
            explanation="Перевезення пасажирів у причепі заборонено."
        )
        questions_dict["e9"] = q
        QuizzesQuestions.objects.create(quiz=quiz_e, question=q)
        
        Answer.objects.create(question=q, text="Так, це дозволено", is_correct=False)
        Answer.objects.create(question=q, text="Так, але тільки в спеціально обладнаному причепі", is_correct=False)
        Answer.objects.create(question=q, text="Ні, це заборонено", is_correct=True)
        Answer.objects.create(question=q, text="Так, але не більше 5 осіб", is_correct=False)
        
        # Вопрос 10
        q = Question.objects.create(
            text="Як правильно виконувати поворот праворуч з причепом?",
            explanation="При повороті праворуч з причепом потрібно збільшити радіус повороту, щоб задні колеса причепа не наїхали на бордюр або інші перешкоди."
        )
        questions_dict["e10"] = q
        QuizzesQuestions.objects.create(quiz=quiz_e, question=q)
        
        Answer.objects.create(question=q, text="Збільшити швидкість перед поворотом", is_correct=False)
        Answer.objects.create(question=q, text="Збільшити радіус повороту", is_correct=True)
        Answer.objects.create(question=q, text="Зменшити радіус повороту", is_correct=False)
        Answer.objects.create(question=q, text="Виконувати поворот як звичайно", is_correct=False)
        
        # Вопрос 11
        q = Question.objects.create(
            text="Що таке 'складання' автопоїзда?",
            explanation="'Складання' автопоїзда - це явище, коли причіп виходить з-під контролю і згинається відносно тягача, створюючи аварійну ситуацію."
        )
        questions_dict["e11"] = q
        QuizzesQuestions.objects.create(quiz=quiz_e, question=q)
        
        Answer.objects.create(question=q, text="Це нормальний маневр автопоїзда", is_correct=False)
        Answer.objects.create(question=q, text="Це процес з'єднання тягача і причепа", is_correct=False)
        Answer.objects.create(question=q, text="Це аварійна ситуація, коли причіп виходить з-під контролю", is_correct=True)
        Answer.objects.create(question=q, text="Це спеціальний режим стоянки автопоїзда", is_correct=False)
        
        # Вопрос 12
        q = Question.objects.create(
            text="Як правильно рухатися заднім ходом з причепом?",
            explanation="При русі заднім ходом з причепом необхідно рухатися повільно і контролювати траєкторію причепа, при необхідності використовуючи допомогу сторонньої особи."
        )
        questions_dict["e12"] = q
        QuizzesQuestions.objects.create(quiz=quiz_e, question=q)
        
        Answer.objects.create(question=q, text="Рухатися швидко, щоб причіп не зміщувався", is_correct=False)
        Answer.objects.create(question=q, text="Рухатися повільно, контролюючи траєкторію причепа", is_correct=True)
        Answer.objects.create(question=q, text="Рухатися швидко, не контролюючи траєкторію причепа", is_correct=False)
        Answer.objects.create(question=q, text="Рухатися повільно, не контролюючи траєкторію причепа", is_correct=False)
        
        print(f"Created {len(questions_dict)} questions for Category E")
        return True
    except Exception as e:
        print(f"Error in create_category_e_data: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Running category_e_questions.py script")
    success = create_category_e_data()
    sys.exit(0 if success else 1)
