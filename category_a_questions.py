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

def create_category_a_data():
    try:
        print("Creating questions for Category A (Мотоциклы)...")
        
        # Находим или создаем квиз для категории А
        quiz_a, created = Quiz.objects.get_or_create(
            category="A",
            defaults={
                "title": "Правила дорожнього руху - категорія A",
                "is_random": False
            }
        )
        
        if created:
            print(f"Created quiz A: {quiz_a.title}")
        else:
            print(f"Found existing quiz A: {quiz_a.title}")
            # Очищаем существующие вопросы для квиза
            QuizzesQuestions.objects.filter(quiz=quiz_a).delete()
            print("Cleared existing questions for Category A")
        
        # Создаем словарь для хранения созданных вопросов
        questions_dict = {}
        
        # Вопрос 1
        q = Question.objects.create(
            text="Яка максимальна швидкість дозволена для мотоциклів на автомагістралях в Україні?",
            explanation="Згідно з ПДР України, на автомагістралях для мотоциклів встановлено обмеження швидкості 130 км/год."
        )
        questions_dict["a1"] = q
        QuizzesQuestions.objects.create(quiz=quiz_a, question=q)
        
        Answer.objects.create(question=q, text="90 км/год", is_correct=False)
        Answer.objects.create(question=q, text="110 км/год", is_correct=False)
        Answer.objects.create(question=q, text="130 км/год", is_correct=True)
        Answer.objects.create(question=q, text="150 км/год", is_correct=False)
        
        # Вопрос 2
        q = Question.objects.create(
            text="Чи може мотоцикліст їхати між рядами транспортних засобів, що стоять або рухаються в заторі?",
            explanation="Рух між рядами транспортних засобів заборонений згідно з ПДР."
        )
        questions_dict["a2"] = q
        QuizzesQuestions.objects.create(quiz=quiz_a, question=q)
        
        Answer.objects.create(question=q, text="Так, але тільки при швидкості до 20 км/год", is_correct=False)
        Answer.objects.create(question=q, text="Так, це дозволено в будь-якому випадку", is_correct=False)
        Answer.objects.create(question=q, text="Ні, це заборонено", is_correct=True)
        
        # Вопрос 3
        q = Question.objects.create(
            text="З якого віку можна керувати мотоциклом (категорія A) в Україні?",
            explanation="Посвідчення водія категорії А можна отримати з 16 років."
        )
        questions_dict["a3"] = q
        QuizzesQuestions.objects.create(quiz=quiz_a, question=q)
        
        Answer.objects.create(question=q, text="14 років", is_correct=False)
        Answer.objects.create(question=q, text="16 років", is_correct=True)
        Answer.objects.create(question=q, text="18 років", is_correct=False)
        Answer.objects.create(question=q, text="21 рік", is_correct=False)
        
        # Вопрос 4
        q = Question.objects.create(
            text="Яке розташування на дорозі є правильним для мотоцикла?",
            explanation="Мотоцикли повинні рухатися в один ряд якомога ближче до правого краю проїзної частини."
        )
        questions_dict["a4"] = q
        QuizzesQuestions.objects.create(quiz=quiz_a, question=q)
        
        Answer.objects.create(question=q, text="В один ряд якомога ближче до правого краю проїзної частини", is_correct=True)
        Answer.objects.create(question=q, text="В один ряд посередині смуги руху", is_correct=False)
        Answer.objects.create(question=q, text="У будь-якому місці смуги руху", is_correct=False)
        Answer.objects.create(question=q, text="Якомога ближче до розділювальної смуги", is_correct=False)
        
        # Вопрос 5
        q = Question.objects.create(
            text="Чи дозволяється перевезення пасажирів на мотоциклі без бокового причепа?",
            explanation="Перевезення пасажирів на мотоциклі без бокового причепа дозволяється на додатковому сидінні."
        )
        questions_dict["a5"] = q
        QuizzesQuestions.objects.create(quiz=quiz_a, question=q)
        
        Answer.objects.create(question=q, text="Не дозволяється в жодному випадку", is_correct=False)
        Answer.objects.create(question=q, text="Дозволяється тільки на додатковому сидінні", is_correct=True)
        Answer.objects.create(question=q, text="Дозволяється в будь-якому випадку", is_correct=False)
        Answer.objects.create(question=q, text="Дозволяється тільки дітей до 12 років", is_correct=False)
        
        # Вопрос 6
        q = Question.objects.create(
            text="Які засоби безпеки обов'язкові для водія мотоцикла?",
            explanation="Для водія мотоцикла обов'язковим є використання мотошолома."
        )
        questions_dict["a6"] = q
        QuizzesQuestions.objects.create(quiz=quiz_a, question=q)
        
        Answer.objects.create(question=q, text="Тільки мотошолом", is_correct=True)
        Answer.objects.create(question=q, text="Мотошолом та захисний жилет", is_correct=False)
        Answer.objects.create(question=q, text="Мотошолом, захисний жилет та рукавиці", is_correct=False)
        Answer.objects.create(question=q, text="Засоби безпеки не обов'язкові", is_correct=False)
        
        # Вопрос 7
        q = Question.objects.create(
            text="Чи дозволяється буксирування мотоцикла?",
            explanation="Буксирування мотоцикла дозволяється тільки в жорсткому зчепленні."
        )
        questions_dict["a7"] = q
        QuizzesQuestions.objects.create(quiz=quiz_a, question=q)
        
        Answer.objects.create(question=q, text="Не дозволяється в жодному випадку", is_correct=False)
        Answer.objects.create(question=q, text="Дозволяється тільки в жорсткому зчепленні", is_correct=True)
        Answer.objects.create(question=q, text="Дозволяється тільки на гнучкому зчепленні", is_correct=False)
        Answer.objects.create(question=q, text="Дозволяється в будь-якому випадку", is_correct=False)
        
        # Вопрос 8
        q = Question.objects.create(
            text="З якої сторони слід сідати на мотоцикл?",
            explanation="На мотоцикл слід сідати з лівого боку."
        )
        questions_dict["a8"] = q
        QuizzesQuestions.objects.create(quiz=quiz_a, question=q)
        
        Answer.objects.create(question=q, text="З правого боку", is_correct=False)
        Answer.objects.create(question=q, text="З лівого боку", is_correct=True)
        Answer.objects.create(question=q, text="З будь-якого боку", is_correct=False)
        Answer.objects.create(question=q, text="Тільки ззаду", is_correct=False)
        
        # Вопрос 9
        q = Question.objects.create(
            text="Яка максимальна швидкість дозволена для мотоциклів на дорогах за межами населених пунктів?",
            explanation="На дорогах за межами населених пунктів для мотоциклів встановлено обмеження швидкості 90 км/год."
        )
        questions_dict["a9"] = q
        QuizzesQuestions.objects.create(quiz=quiz_a, question=q)
        
        Answer.objects.create(question=q, text="60 км/год", is_correct=False)
        Answer.objects.create(question=q, text="90 км/год", is_correct=True)
        Answer.objects.create(question=q, text="110 км/год", is_correct=False)
        Answer.objects.create(question=q, text="130 км/год", is_correct=False)
        
        # Вопрос 10
        q = Question.objects.create(
            text="Чи можна керувати мотоциклом, тримаючись за кермо однією рукою?",
            explanation="Керувати мотоциклом, тримаючись за кермо однією рукою, заборонено."
        )
        questions_dict["a10"] = q
        QuizzesQuestions.objects.create(quiz=quiz_a, question=q)
        
        Answer.objects.create(question=q, text="Так, це дозволено", is_correct=False)
        Answer.objects.create(question=q, text="Так, але тільки при швидкості до 40 км/год", is_correct=False)
        Answer.objects.create(question=q, text="Ні, це заборонено", is_correct=True)
        Answer.objects.create(question=q, text="Так, але тільки поза населеними пунктами", is_correct=False)
        
        # Вопрос 11
        q = Question.objects.create(
            text="Яка мінімальна дистанція між мотоциклами під час руху в колоні?",
            explanation="Мінімальна дистанція між мотоциклами під час руху в колоні повинна бути не менше 10 метрів."
        )
        questions_dict["a11"] = q
        QuizzesQuestions.objects.create(quiz=quiz_a, question=q)
        
        Answer.objects.create(question=q, text="5 метрів", is_correct=False)
        Answer.objects.create(question=q, text="10 метрів", is_correct=True)
        Answer.objects.create(question=q, text="15 метрів", is_correct=False)
        Answer.objects.create(question=q, text="20 метрів", is_correct=False)
        
        # Вопрос 12
        q = Question.objects.create(
            text="Чи дозволяється перевезення дітей до 12 років на мотоциклі?",
            explanation="Перевезення дітей до 12 років на мотоциклі дозволяється за умови, що вони сидять у боковому причепі."
        )
        questions_dict["a12"] = q
        QuizzesQuestions.objects.create(quiz=quiz_a, question=q)
        
        Answer.objects.create(question=q, text="Не дозволяється в жодному випадку", is_correct=False)
        Answer.objects.create(question=q, text="Дозволяється тільки в боковому причепі", is_correct=True)
        Answer.objects.create(question=q, text="Дозволяється на додатковому сидінні", is_correct=False)
        Answer.objects.create(question=q, text="Дозволяється в будь-якому випадку", is_correct=False)
        
        # Вопрос 13
        q = Question.objects.create(
            text="Яка максимальна дозволена ширина мотоцикла з боковим причепом?",
            explanation="Максимальна дозволена ширина мотоцикла з боковим причепом становить 2 метри."
        )
        questions_dict["a13"] = q
        QuizzesQuestions.objects.create(quiz=quiz_a, question=q)
        
        Answer.objects.create(question=q, text="1,5 метра", is_correct=False)
        Answer.objects.create(question=q, text="2 метри", is_correct=True)
        Answer.objects.create(question=q, text="2,5 метра", is_correct=False)
        Answer.objects.create(question=q, text="3 метри", is_correct=False)
        
        # Вопрос 14
        q = Question.objects.create(
            text="Чи дозволяється рух мотоциклів по тротуарах і пішохідних доріжках?",
            explanation="Рух мотоциклів по тротуарах і пішохідних доріжках заборонено."
        )
        questions_dict["a14"] = q
        QuizzesQuestions.objects.create(quiz=quiz_a, question=q)
        
        Answer.objects.create(question=q, text="Так, це дозволено", is_correct=False)
        Answer.objects.create(question=q, text="Так, але тільки при швидкості до 5 км/год", is_correct=False)
        Answer.objects.create(question=q, text="Ні, це заборонено", is_correct=True)
        Answer.objects.create(question=q, text="Так, але тільки для об'їзду перешкод", is_correct=False)
        
        # Вопрос 15
        q = Question.objects.create(
            text="Яка максимальна дозволена швидкість для мотоциклів у житлових зонах?",
            explanation="У житлових зонах максимальна дозволена швидкість для всіх транспортних засобів, включаючи мотоцикли, становить 20 км/год."
        )
        questions_dict["a15"] = q
        QuizzesQuestions.objects.create(quiz=quiz_a, question=q)
        
        Answer.objects.create(question=q, text="20 км/год", is_correct=True)
        Answer.objects.create(question=q, text="30 км/год", is_correct=False)
        Answer.objects.create(question=q, text="40 км/год", is_correct=False)
        Answer.objects.create(question=q, text="50 км/год", is_correct=False)
        
        # Вопрос 16
        q = Question.objects.create(
            text="Що необхідно зробити перед запуском двигуна мотоцикла?",
            explanation="Перед запуском двигуна мотоцикла необхідно переконатися, що увімкнений нейтральний режим коробки передач."
        )
        questions_dict["a16"] = q
        QuizzesQuestions.objects.create(quiz=quiz_a, question=q)
        
        Answer.objects.create(question=q, text="Увімкнути першу передачу", is_correct=False)
        Answer.objects.create(question=q, text="Переконатися, що увімкнений нейтральний режим", is_correct=True)
        Answer.objects.create(question=q, text="Встановити максимальні оберти", is_correct=False)
        Answer.objects.create(question=q, text="Від'єднати зчеплення", is_correct=False)
        
        # Вопрос 17
        q = Question.objects.create(
            text="Чи дозволяється мотоциклісту перевозити вантаж, що виступає більш ніж на 0,5 м за габарити?",
            explanation="Перевезення вантажу, що виступає більш ніж на 0,5 м за габарити мотоцикла по довжині або ширині, заборонено."
        )
        questions_dict["a17"] = q
        QuizzesQuestions.objects.create(quiz=quiz_a, question=q)
        
        Answer.objects.create(question=q, text="Так, це дозволено", is_correct=False)
        Answer.objects.create(question=q, text="Ні, це заборонено", is_correct=True)
        Answer.objects.create(question=q, text="Так, але тільки в світлу пору доби", is_correct=False)
        Answer.objects.create(question=q, text="Так, але тільки при наявності спеціального позначення", is_correct=False)
        
        # Вопрос 18
        q = Question.objects.create(
            text="Як правильно гальмувати на мотоциклі під час повороту?",
            explanation="Під час повороту на мотоциклі рекомендується гальмувати переважно заднім гальмом, щоб уникнути блокування переднього колеса."
        )
        questions_dict["a18"] = q
        QuizzesQuestions.objects.create(quiz=quiz_a, question=q)
        
        Answer.objects.create(question=q, text="Тільки переднім гальмом", is_correct=False)
        Answer.objects.create(question=q, text="Тільки заднім гальмом", is_correct=True)
        Answer.objects.create(question=q, text="Обома гальмами одночасно", is_correct=False)
        Answer.objects.create(question=q, text="Не гальмувати під час повороту взагалі", is_correct=False)
        
        # Вопрос 19
        q = Question.objects.create(
            text="Яке світло повинен використовувати мотоцикліст у світлу пору доби?",
            explanation="У світлу пору доби на мотоциклі повинно бути увімкнене ближнє світло фар або денні ходові вогні."
        )
        questions_dict["a19"] = q
        QuizzesQuestions.objects.create(quiz=quiz_a, question=q)
        
        Answer.objects.create(question=q, text="Ближнє світло фар або денні ходові вогні", is_correct=True)
        Answer.objects.create(question=q, text="Дальнє світло фар", is_correct=False)
        Answer.objects.create(question=q, text="Габаритні вогні", is_correct=False)
        Answer.objects.create(question=q, text="Світло можна не вмикати", is_correct=False)
        
        # Вопрос 20
        q = Question.objects.create(
            text="Чи дозволяється мотоциклісту під час руху відпускати кермо?",
            explanation="Мотоциклісту заборонено під час руху відпускати кермо або піднімати переднє колесо."
        )
        questions_dict["a20"] = q
        QuizzesQuestions.objects.create(quiz=quiz_a, question=q)
        
        Answer.objects.create(question=q, text="Так, це дозволено", is_correct=False)
        Answer.objects.create(question=q, text="Ні, це заборонено", is_correct=True)
        Answer.objects.create(question=q, text="Так, але тільки на короткий час", is_correct=False)
        Answer.objects.create(question=q, text="Так, але тільки при швидкості до 20 км/год", is_correct=False)
        
        print(f"Created {len(questions_dict)} questions for Category A")
        return True
    except Exception as e:
        print(f"Error in create_category_a_data: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Running category_a_questions.py script")
    success = create_category_a_data()
    sys.exit(0 if success else 1)
