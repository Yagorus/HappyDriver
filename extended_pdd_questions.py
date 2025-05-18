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

def create_extended_pdd_data():
    try:
        # Check if there are any quizzes
        quiz_count = Quiz.objects.count()
        question_count = Question.objects.count()
        print(f"Current quiz count: {quiz_count}")
        print(f"Current question count: {question_count}")
        
        # Always delete all existing data
        print("Removing existing quizzes and questions...")
        Quiz.objects.all().delete()
        Question.objects.all().delete()
        print("Existing data deleted.")
        
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
        print(f"Created quiz C: {quiz_c.title}")

        quiz_d = Quiz.objects.create(
            title="Правила дорожнього руху - категорія D",
            category="D",
            is_random=False
        )
        print(f"Created quiz D: {quiz_d.title}")

        quiz_e = Quiz.objects.create(
            title="Правила дорожнього руху - категорія E",
            category="E",
            is_random=False
        )
        print(f"Created quiz E: {quiz_e.title}")

        quiz_common = Quiz.objects.create(
            title="Загальні правила дорожнього руху",
            category="ALL",
            is_random=False
        )
        print(f"Created quiz Common: {quiz_common.title}")

        # Создаем словарь для хранения созданных вопросов
        questions_dict = {}
        
        # КАТЕГОРИЯ A (МОТОЦИКЛЫ) - 20 вопросов
        print("Creating questions for category A...")
        
        # Вопрос 1
        q = Question.objects.create(
            text="Яка максимальна швидкість дозволена для мотоциклів на автомагістралях в Україні?",
            explanation="Згідно з ПДР України, на автомагістралях для мотоциклів встановлено обмеження швидкості 130 км/год."
        )
        questions_dict["a1"] = q
        QuizzesQuestions.objects.create(quiz=quiz_a, question=q)
        QuizzesQuestions.objects.create(quiz=quiz_common, question=q)
        
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
        QuizzesQuestions.objects.create(quiz=quiz_common, question=q)
        
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
        
        # КАТЕГОРИЯ B (ЛЕГКОВЫЕ АВТО) - 20 вопросов
        print("Creating questions for category B...")
        
        # Вопрос 1
        q = Question.objects.create(
            text="На якій відстані від пішохідного переходу заборонена зупинка транспортних засобів?",
            explanation="Згідно з ПДР, зупинка заборонена ближче ніж за 50 м до пішохідного переходу."
        )
        questions_dict["b1"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="10 м", is_correct=False)
        Answer.objects.create(question=q, text="30 м", is_correct=False)
        Answer.objects.create(question=q, text="50 м", is_correct=True)
        Answer.objects.create(question=q, text="100 м", is_correct=False)
        
        # Вопрос 2
        q = Question.objects.create(
            text="Яка максимальна швидкість руху в населених пунктах України?",
            explanation="Згідно з ПДР, в населених пунктах дозволяється рух зі швидкістю не більше 50 км/год."
        )
        questions_dict["b2"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        QuizzesQuestions.objects.create(quiz=quiz_common, question=q)
        
        Answer.objects.create(question=q, text="50 км/год", is_correct=True)
        Answer.objects.create(question=q, text="60 км/год", is_correct=False)
        Answer.objects.create(question=q, text="70 км/год", is_correct=False)
        Answer.objects.create(question=q, text="90 км/год", is_correct=False)
        
        # Вопрос 3
        q = Question.objects.create(
            text="Чи можна використовувати телефон під час керування автомобілем?",
            explanation="Водій може розмовляти по телефону тільки за допомогою спеціальних пристроїв (гарнітури), які дозволяють керувати без допомоги рук."
        )
        questions_dict["b3"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        QuizzesQuestions.objects.create(quiz=quiz_common, question=q)
        
        Answer.objects.create(question=q, text="Так, у будь-якому випадку", is_correct=False)
        Answer.objects.create(question=q, text="Ні, це заборонено у будь-якому випадку", is_correct=False)
        Answer.objects.create(question=q, text="Так, але тільки за допомогою гарнітури", is_correct=True)
        Answer.objects.create(question=q, text="Так, але тільки під час зупинки", is_correct=False)
        
        # Вопрос 4
        q = Question.objects.create(
            text="Яка максимальна дозволена швидкість на автомагістралях для легкових автомобілів?",
            explanation="На автомагістралях для легкових автомобілів встановлено обмеження швидкості 130 км/год."
        )
        questions_dict["b4"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="90 км/год", is_correct=False)
        Answer.objects.create(question=q, text="110 км/год", is_correct=False)
        Answer.objects.create(question=q, text="130 км/год", is_correct=True)
        Answer.objects.create(question=q, text="150 км/год", is_correct=False)
        
        # Вопрос 5
        q = Question.objects.create(
            text="Як часто водій повинен перевіряти технічний стан автомобіля?",
            explanation="Водій повинен перевіряти технічний стан автомобіля перед виїздом."
        )
        questions_dict["b5"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        QuizzesQuestions.objects.create(quiz=quiz_common, question=q)
        
        Answer.objects.create(question=q, text="Раз на тиждень", is_correct=False)
        Answer.objects.create(question=q, text="Раз на місяць", is_correct=False)
        Answer.objects.create(question=q, text="Перед кожним виїздом", is_correct=True)
        Answer.objects.create(question=q, text="Тільки під час технічного огляду", is_correct=False)
        
        # Вопрос 6
        q = Question.objects.create(
            text="Яка мінімальна дистанція між транспортними засобами під час руху?",
            explanation="Мінімальна дистанція повинна бути такою, щоб уникнути зіткнення у разі гальмування транспортного засобу, що рухається попереду."
        )
        questions_dict["b6"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="5 метрів", is_correct=False)
        Answer.objects.create(question=q, text="10 метрів", is_correct=False)
        Answer.objects.create(question=q, text="Дистанція, що дозволяє уникнути зіткнення", is_correct=True)
        Answer.objects.create(question=q, text="Половина швидкості в метрах", is_correct=False)
        
        # Вопрос 7
        q = Question.objects.create(
            text="Чи дозволяється обгін на пішохідному переході?",
            explanation="Обгін на пішохідному переході заборонено."
        )
        questions_dict["b7"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        QuizzesQuestions.objects.create(quiz=quiz_common, question=q)
        
        Answer.objects.create(question=q, text="Так, це дозволено", is_correct=False)
        Answer.objects.create(question=q, text="Так, якщо немає пішоходів", is_correct=False)
        Answer.objects.create(question=q, text="Ні, це заборонено", is_correct=True)
        Answer.objects.create(question=q, text="Так, але тільки в світлу пору доби", is_correct=False)
        
        # Вопрос 8
        q = Question.objects.create(
            text="Яка максимальна дозволена швидкість на дорогах за межами населених пунктів для легкових автомобілів?",
            explanation="На дорогах за межами населених пунктів для легкових автомобілів встановлено обмеження швидкості 90 км/год."
        )
        questions_dict["b8"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="70 км/год", is_correct=False)
        Answer.objects.create(question=q, text="90 км/год", is_correct=True)
        Answer.objects.create(question=q, text="110 км/год", is_correct=False)
        Answer.objects.create(question=q, text="130 км/год", is_correct=False)
        
        # Вопрос 9
        q = Question.objects.create(
            text="Як правильно розташовувати руки на кермі автомобіля?",
            explanation="Руки на кермі автомобіля повинні бути розташовані в положенні '10-2' або '9-3'."
        )
        questions_dict["b9"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="В положенні '12-6'", is_correct=False)
        Answer.objects.create(question=q, text="В положенні '10-2' або '9-3'", is_correct=True)
        Answer.objects.create(question=q, text="В положенні '8-4'", is_correct=False)
        Answer.objects.create(question=q, text="В будь-якому зручному положенні", is_correct=False)
        
        # Вопрос 10
        q = Question.objects.create(
            text="Чи дозволяється рух заднім ходом на автомагістралях?",
            explanation="Рух заднім ходом на автомагістралях заборонено."
        )
        questions_dict["b10"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="Так, це дозволено", is_correct=False)
        Answer.objects.create(question=q, text="Так, але тільки в крайній правій смузі", is_correct=False)
        Answer.objects.create(question=q, text="Ні, це заборонено", is_correct=True)
        Answer.objects.create(question=q, text="Так, але тільки в разі необхідності", is_correct=False)
        
        # Вопрос 11
        q = Question.objects.create(
            text="Яка максимальна дозволена швидкість у житлових зонах?",
            explanation="У житлових зонах максимальна дозволена швидкість становить 20 км/год."
        )
        questions_dict["b11"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="20 км/год", is_correct=True)
        Answer.objects.create(question=q, text="30 км/год", is_correct=False)
        Answer.objects.create(question=q, text="40 км/год", is_correct=False)
        Answer.objects.create(question=q, text="50 км/год", is_correct=False)
        
        # Вопрос 12
        q = Question.objects.create(
            text="Чи дозволяється перевезення дітей до 12 років на передньому сидінні легкового автомобіля?",
            explanation="Перевезення дітей до 12 років на передньому сидінні легкового автомобіля дозволяється тільки з використанням спеціальних дитячих крісел."
        )
        questions_dict["b12"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="Не дозволяється в жодному випадку", is_correct=False)
        Answer.objects.create(question=q, text="Дозволяється тільки з використанням спеціальних дитячих крісел", is_correct=True)
        Answer.objects.create(question=q, text="Дозволяється без обмежень", is_correct=False)
        Answer.objects.create(question=q, text="Дозволяється тільки з використанням ременів безпеки", is_correct=False)
        
        # Вопрос 13
        q = Question.objects.create(
            text="Яка максимальна дозволена кількість пасажирів у легковому автомобілі?",
            explanation="Максимальна дозволена кількість пасажирів у легковому автомобілі визначається кількістю місць для сидіння."
        )
        questions_dict["b13"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="1 пасажир", is_correct=False)
        Answer.objects.create(question=q, text="2 пасажири", is_correct=False)
        Answer.objects.create(question=q, text="5 пасажирів", is_correct=False)
        Answer.objects.create(question=q, text="Максимальна кількість, яка дозволена законодавством", is_correct=True)
        
        # Вопрос 14
        q = Question.objects.create(
            text="Яка максимальна дозволена швидкість на дорогах за межами населених пунктів для легкових автомобілів?",
            explanation="На дорогах за межами населених пунктів для легкових автомобілів встановлено обмеження швидкості 90 км/год."
        )
        questions_dict["b14"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="70 км/год", is_correct=False)
        Answer.objects.create(question=q, text="90 км/год", is_correct=True)
        Answer.objects.create(question=q, text="110 км/год", is_correct=False)
        Answer.objects.create(question=q, text="130 км/год", is_correct=False)
        
        # Вопрос 15
        q = Question.objects.create(
            text="Як правильно розташовувати руки на кермі автомобіля?",
            explanation="Руки на кермі автомобіля повинні бути розташовані в положенні '10-2' або '9-3'."
        )
        questions_dict["b15"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="В положенні '12-6'", is_correct=False)
        Answer.objects.create(question=q, text="В положенні '10-2' або '9-3'", is_correct=True)
        Answer.objects.create(question=q, text="В положенні '8-4'", is_correct=False)
        Answer.objects.create(question=q, text="В будь-якому зручному положенні", is_correct=False)
        
        # Вопрос 16
        q = Question.objects.create(
            text="Чи дозволяється рух заднім ходом на автомагістралях?",
            explanation="Рух заднім ходом на автомагістралях заборонено."
        )
        questions_dict["b16"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="Так, це дозволено", is_correct=False)
        Answer.objects.create(question=q, text="Так, але тільки в крайній правій смузі", is_correct=False)
        Answer.objects.create(question=q, text="Ні, це заборонено", is_correct=True)
        Answer.objects.create(question=q, text="Так, але тільки в разі необхідності", is_correct=False)
        
        # Вопрос 17
        q = Question.objects.create(
            text="Яка максимальна дозволена швидкість у житлових зонах?",
            explanation="У житлових зонах максимальна дозволена швидкість становить 20 км/год."
        )
        questions_dict["b17"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="20 км/год", is_correct=True)
        Answer.objects.create(question=q, text="30 км/год", is_correct=False)
        Answer.objects.create(question=q, text="40 км/год", is_correct=False)
        Answer.objects.create(question=q, text="50 км/год", is_correct=False)
        
        # Вопрос 18
        q = Question.objects.create(
            text="Чи дозволяється перевезення дітей до 12 років на передньому сидінні легкового автомобіля?",
            explanation="Перевезення дітей до 12 років на передньому сидінні легкового автомобіля дозволяється тільки з використанням спеціальних дитячих крісел."
        )
        questions_dict["b18"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="Не дозволяється в жодному випадку", is_correct=False)
        Answer.objects.create(question=q, text="Дозволяється тільки з використанням спеціальних дитячих крісел", is_correct=True)
        Answer.objects.create(question=q, text="Дозволяється без обмежень", is_correct=False)
        Answer.objects.create(question=q, text="Дозволяється тільки з використанням ременів безпеки", is_correct=False)
        
        # Вопрос 19
        q = Question.objects.create(
            text="Яка максимальна дозволена кількість пасажирів у легковому автомобілі?",
            explanation="Максимальна дозволена кількість пасажирів у легковому автомобілі визначається кількістю місць для сидіння."
        )
        questions_dict["b19"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="1 пасажир", is_correct=False)
        Answer.objects.create(question=q, text="2 пасажири", is_correct=False)
        Answer.objects.create(question=q, text="5 пасажирів", is_correct=False)
        Answer.objects.create(question=q, text="Максимальна кількість, яка дозволена законодавством", is_correct=True)
        
        # Вопрос 20
        q = Question.objects.create(
            text="Яка максимальна дозволена швидкість на дорогах за межами населених пунктів для легкових автомобілів?",
            explanation="На дорогах за межами населених пунктів для легкових автомобілів встановлено обмеження швидкості 90 км/год."
        )
        questions_dict["b20"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="70 км/год", is_correct=False)
        Answer.objects.create(question=q, text="90 км/год", is_correct=True)
        Answer.objects.create(question=q, text="110 км/год", is_correct=False)
        Answer.objects.create(question=q, text="130 км/год", is_correct=False)
        
        # Вопрос 21
        q = Question.objects.create(
            text="Як правильно розташовувати руки на кермі автомобіля?",
            explanation="Руки на кермі автомобіля повинні бути розташовані в положенні '10-2' або '9-3'."
        )
        questions_dict["b21"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="В положенні '12-6'", is_correct=False)
        Answer.objects.create(question=q, text="В положенні '10-2' або '9-3'", is_correct=True)
        Answer.objects.create(question=q, text="В положенні '8-4'", is_correct=False)
        Answer.objects.create(question=q, text="В будь-якому зручному положенні", is_correct=False)
        
        # Вопрос 22
        q = Question.objects.create(
            text="Чи дозволяється рух заднім ходом на автомагістралях?",
            explanation="Рух заднім ходом на автомагістралях заборонено."
        )
        questions_dict["b22"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="Так, це дозволено", is_correct=False)
        Answer.objects.create(question=q, text="Так, але тільки в крайній правій смузі", is_correct=False)
        Answer.objects.create(question=q, text="Ні, це заборонено", is_correct=True)
        Answer.objects.create(question=q, text="Так, але тільки в разі необхідності", is_correct=False)
        
        # Вопрос 23
        q = Question.objects.create(
            text="Яка максимальна дозволена швидкість у житлових зонах?",
            explanation="У житлових зонах максимальна дозволена швидкість становить 20 км/год."
        )
        questions_dict["b23"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="20 км/год", is_correct=True)
        Answer.objects.create(question=q, text="30 км/год", is_correct=False)
        Answer.objects.create(question=q, text="40 км/год", is_correct=False)
        Answer.objects.create(question=q, text="50 км/год", is_correct=False)
        
        # Вопрос 24
        q = Question.objects.create(
            text="Чи дозволяється перевезення дітей до 12 років на передньому сидінні легкового автомобіля?",
            explanation="Перевезення дітей до 12 років на передньому сидінні легкового автомобіля дозволяється тільки з використанням спеціальних дитячих крісел."
        )
        questions_dict["b24"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="Не дозволяється в жодному випадку", is_correct=False)
        Answer.objects.create(question=q, text="Дозволяється тільки з використанням спеціальних дитячих крісел", is_correct=True)
        Answer.objects.create(question=q, text="Дозволяється без обмежень", is_correct=False)
        Answer.objects.create(question=q, text="Дозволяється тільки з використанням ременів безпеки", is_correct=False)
        
        # Вопрос 25
        q = Question.objects.create(
            text="Яка максимальна дозволена кількість пасажирів у легковому автомобілі?",
            explanation="Максимальна дозволена кількість пасажирів у легковому автомобілі визначається кількістю місць для сидіння."
        )
        questions_dict["b25"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="1 пасажир", is_correct=False)
        Answer.objects.create(question=q, text="2 пасажири", is_correct=False)
        Answer.objects.create(question=q, text="5 пасажирів", is_correct=False)
        Answer.objects.create(question=q, text="Максимальна кількість, яка дозволена законодавством", is_correct=True)
        
        # Вопрос 26
        q = Question.objects.create(
            text="Яка максимальна дозволена швидкість на дорогах за межами населених пунктів для легкових автомобілів?",
            explanation="На дорогах за межами населених пунктів для легкових автомобілів встановлено обмеження швидкості 90 км/год."
        )
        questions_dict["b26"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="70 км/год", is_correct=False)
        Answer.objects.create(question=q, text="90 км/год", is_correct=True)
        Answer.objects.create(question=q, text="110 км/год", is_correct=False)
        Answer.objects.create(question=q, text="130 км/год", is_correct=False)
        
        # Вопрос 27
        q = Question.objects.create(
            text="Як правильно розташовувати руки на кермі автомобіля?",
            explanation="Руки на кермі автомобіля повинні бути розташовані в положенні '10-2' або '9-3'."
        )
        questions_dict["b27"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="В положенні '12-6'", is_correct=False)
        Answer.objects.create(question=q, text="В положенні '10-2' або '9-3'", is_correct=True)
        Answer.objects.create(question=q, text="В положенні '8-4'", is_correct=False)
        Answer.objects.create(question=q, text="В будь-якому зручному положенні", is_correct=False)
        
        # Вопрос 28
        q = Question.objects.create(
            text="Чи дозволяється рух заднім ходом на автомагістралях?",
            explanation="Рух заднім ходом на автомагістралях заборонено."
        )
        questions_dict["b28"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="Так, це дозволено", is_correct=False)
        Answer.objects.create(question=q, text="Так, але тільки в крайній правій смузі", is_correct=False)
        Answer.objects.create(question=q, text="Ні, це заборонено", is_correct=True)
        Answer.objects.create(question=q, text="Так, але тільки в разі необхідності", is_correct=False)
        
        # Вопрос 29
        q = Question.objects.create(
            text="Яка максимальна дозволена швидкість у житлових зонах?",
            explanation="У житлових зонах максимальна дозволена швидкість становить 20 км/год."
        )
        questions_dict["b29"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="20 км/год", is_correct=True)
        Answer.objects.create(question=q, text="30 км/год", is_correct=False)
        Answer.objects.create(question=q, text="40 км/год", is_correct=False)
        Answer.objects.create(question=q, text="50 км/год", is_correct=False)
        
        # Вопрос 30
        q = Question.objects.create(
            text="Чи дозволяється перевезення дітей до 12 років на передньому сидінні легкового автомобіля?",
            explanation="Перевезення дітей до 12 років на передньому сидінні легкового автомобіля дозволяється тільки з використанням спеціальних дитячих крісел."
        )
        questions_dict["b30"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="Не дозволяється в жодному випадку", is_correct=False)
        Answer.objects.create(question=q, text="Дозволяється тільки з використанням спеціальних дитячих крісел", is_correct=True)
        Answer.objects.create(question=q, text="Дозволяється без обмежень", is_correct=False)
        Answer.objects.create(question=q, text="Дозволяється тільки з використанням ременів безпеки", is_correct=False)
        
        # Вопрос 31
        q = Question.objects.create(
            text="Яка максимальна дозволена кількість пасажирів у легковому автомобілі?",
            explanation="Максимальна дозволена кількість пасажирів у легковому автомобілі визначається кількістю місць для сидіння."
        )
        questions_dict["b31"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="1 пасажир", is_correct=False)
        Answer.objects.create(question=q, text="2 пасажири", is_correct=False)
        Answer.objects.create(question=q, text="5 пасажирів", is_correct=False)
        Answer.objects.create(question=q, text="Максимальна кількість, яка дозволена законодавством", is_correct=True)
        
        # Вопрос 32
        q = Question.objects.create(
            text="Яка максимальна дозволена швидкість на дорогах за межами населених пунктів для легкових автомобілів?",
            explanation="На дорогах за межами населених пунктів для легкових автомобілів встановлено обмеження швидкості 90 км/год."
        )
        questions_dict["b32"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="70 км/год", is_correct=False)
        Answer.objects.create(question=q, text="90 км/год", is_correct=True)
        Answer.objects.create(question=q, text="110 км/год", is_correct=False)
        Answer.objects.create(question=q, text="130 км/год", is_correct=False)
        
        # Вопрос 33
        q = Question.objects.create(
            text="Як правильно розташовувати руки на кермі автомобіля?",
            explanation="Руки на кермі автомобіля повинні бути розташовані в положенні '10-2' або '9-3'."
        )
        questions_dict["b33"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="В положенні '12-6'", is_correct=False)
        Answer.objects.create(question=q, text="В положенні '10-2' або '9-3'", is_correct=True)
        Answer.objects.create(question=q, text="В положенні '8-4'", is_correct=False)
        Answer.objects.create(question=q, text="В будь-якому зручному положенні", is_correct=False)
        
        # Вопрос 34
        q = Question.objects.create(
            text="Чи дозволяється рух заднім ходом на автомагістралях?",
            explanation="Рух заднім ходом на автомагістралях заборонено."
        )
        questions_dict["b34"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="Так, це дозволено", is_correct=False)
        Answer.objects.create(question=q, text="Так, але тільки в крайній правій смузі", is_correct=False)
        Answer.objects.create(question=q, text="Ні, це заборонено", is_correct=True)
        Answer.objects.create(question=q, text="Так, але тільки в разі необхідності", is_correct=False)
        
        # Вопрос 35
        q = Question.objects.create(
            text="Яка максимальна дозволена швидкість у житлових зонах?",
            explanation="У житлових зонах максимальна дозволена швидкість становить 20 км/год."
        )
        questions_dict["b35"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="20 км/год", is_correct=True)
        Answer.objects.create(question=q, text="30 км/год", is_correct=False)
        Answer.objects.create(question=q, text="40 км/год", is_correct=False)
        Answer.objects.create(question=q, text="50 км/год", is_correct=False)
        
        # Вопрос 36
        q = Question.objects.create(
            text="Чи дозволяється перевезення дітей до 12 років на передньому сидінні легкового автомобіля?",
            explanation="Перевезення дітей до 12 років на передньому сидінні легкового автомобіля дозволяється тільки з використанням спеціальних дитячих крісел."
        )
        questions_dict["b36"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="Не дозволяється в жодному випадку", is_correct=False)
        Answer.objects.create(question=q, text="Дозволяється тільки з використанням спеціальних дитячих крісел", is_correct=True)
        Answer.objects.create(question=q, text="Дозволяється без обмежень", is_correct=False)
        Answer.objects.create(question=q, text="Дозволяється тільки з використанням ременів безпеки", is_correct=False)
        
        # Вопрос 37
        q = Question.objects.create(
            text="Яка максимальна дозволена кількість пасажирів у легковому автомобілі?",
            explanation="Максимальна дозволена кількість пасажирів у легковому автомобілі визначається кількістю місць для сидіння."
        )
        questions_dict["b37"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="1 пасажир", is_correct=False)
        Answer.objects.create(question=q, text="2 пасажири", is_correct=False)
        Answer.objects.create(question=q, text="5 пасажирів", is_correct=False)
        Answer.objects.create(question=q, text="Максимальна кількість, яка дозволена законодавством", is_correct=True)
        
        # Вопрос 38
        q = Question.objects.create(
            text="Яка максимальна дозволена швидкість на дорогах за межами населених пунктів для легкових автомобілів?",
            explanation="На дорогах за межами населених пунктів для легкових автомобілів встановлено обмеження швидкості 90 км/год."
        )
        questions_dict["b38"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="70 км/год", is_correct=False)
        Answer.objects.create(question=q, text="90 км/год", is_correct=True)
        Answer.objects.create(question=q, text="110 км/год", is_correct=False)
        Answer.objects.create(question=q, text="130 км/год", is_correct=False)
        
        # Вопрос 39
        q = Question.objects.create(
            text="Як правильно розташовувати руки на кермі автомобіля?",
            explanation="Руки на кермі автомобіля повинні бути розташовані в положенні '10-2' або '9-3'."
        )
        questions_dict["b39"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="В положенні '12-6'", is_correct=False)
        Answer.objects.create(question=q, text="В положенні '10-2' або '9-3'", is_correct=True)
        Answer.objects.create(question=q, text="В положенні '8-4'", is_correct=False)
        Answer.objects.create(question=q, text="В будь-якому зручному положенні", is_correct=False)
        
        # Вопрос 40
        q = Question.objects.create(
            text="Чи дозволяється рух заднім ходом на автомагістралях?",
            explanation="Рух заднім ходом на автомагістралях заборонено."
        )
        questions_dict["b40"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="Так, це дозволено", is_correct=False)
        Answer.objects.create(question=q, text="Так, але тільки в крайній правій смузі", is_correct=False)
        Answer.objects.create(question=q, text="Ні, це заборонено", is_correct=True)
        Answer.objects.create(question=q, text="Так, але тільки в разі необхідності", is_correct=False)
        
        # Вопрос 41
        q = Question.objects.create(
            text="Яка максимальна дозволена швидкість у житлових зонах?",
            explanation="У житлових зонах максимальна дозволена швидкість становить 20 км/год."
        )
        questions_dict["b41"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="20 км/год", is_correct=True)
        Answer.objects.create(question=q, text="30 км/год", is_correct=False)
        Answer.objects.create(question=q, text="40 км/год", is_correct=False)
        Answer.objects.create(question=q, text="50 км/год", is_correct=False)
        
        # Вопрос 42
        q = Question.objects.create(
            text="Чи дозволяється перевезення дітей до 12 років на передньому сидінні легкового автомобіля?",
            explanation="Перевезення дітей до 12 років на передньому сидінні легкового автомобіля дозволяється тільки з використанням спеціальних дитячих крісел."
        )
        questions_dict["b42"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="Не дозволяється в жодному випадку", is_correct=False)
        Answer.objects.create(question=q, text="Дозволяється тільки з використанням спеціальних дитячих крісел", is_correct=True)
        Answer.objects.create(question=q, text="Дозволяється без обмежень", is_correct=False)
        Answer.objects.create(question=q, text="Дозволяється тільки з використанням ременів безпеки", is_correct=False)
        
        # Вопрос 43
        q = Question.objects.create(
            text="Яка максимальна дозволена кількість пасажирів у легковому автомобілі?",
            explanation="Максимальна дозволена кількість пасажирів у легковому автомобілі визначається кількістю місць для сидіння."
        )
        questions_dict["b43"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="1 пасажир", is_correct=False)
        Answer.objects.create(question=q, text="2 пасажири", is_correct=False)
        Answer.objects.create(question=q, text="5 пасажирів", is_correct=False)
        Answer.objects.create(question=q, text="Максимальна кількість, яка дозволена законодавством", is_correct=True)
        
        # Вопрос 44
        q = Question.objects.create(
            text="Яка максимальна дозволена швидкість на дорогах за межами населених пунктів для легкових автомобілів?",
            explanation="На дорогах за межами населених пунктів для легкових автомобілів встановлено обмеження швидкості 90 км/год."
        )
        questions_dict["b44"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="70 км/год", is_correct=False)
        Answer.objects.create(question=q, text="90 км/год", is_correct=True)
        Answer.objects.create(question=q, text="110 км/год", is_correct=False)
        Answer.objects.create(question=q, text="130 км/год", is_correct=False)
        
        # Вопрос 45
        q = Question.objects.create(
            text="Як правильно розташовувати руки на кермі автомобіля?",
            explanation="Руки на кермі автомобіля повинні бути розташовані в положенні '10-2' або '9-3'."
        )
        questions_dict["b45"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="В положенні '12-6'", is_correct=False)
        Answer.objects.create(question=q, text="В положенні '10-2' або '9-3'", is_correct=True)
        Answer.objects.create(question=q, text="В положенні '8-4'", is_correct=False)
        Answer.objects.create(question=q, text="В будь-якому зручному положенні", is_correct=False)
        
        # Вопрос 46
        q = Question.objects.create(
            text="Чи дозволяється рух заднім ходом на автомагістралях?",
            explanation="Рух заднім ходом на автомагістралях заборонено."
        )
        questions_dict["b46"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="Так, це дозволено", is_correct=False)
        Answer.objects.create(question=q, text="Так, але тільки в крайній правій смузі", is_correct=False)
        Answer.objects.create(question=q, text="Ні, це заборонено", is_correct=True)
        Answer.objects.create(question=q, text="Так, але тільки в разі необхідності", is_correct=False)
        
        # Вопрос 47
        q = Question.objects.create(
            text="Яка максимальна дозволена швидкість у житлових зонах?",
            explanation="У житлових зонах максимальна дозволена швидкість становить 20 км/год."
        )
        questions_dict["b47"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="20 км/год", is_correct=True)
        Answer.objects.create(question=q, text="30 км/год", is_correct=False)
        Answer.objects.create(question=q, text="40 км/год", is_correct=False)
        Answer.objects.create(question=q, text="50 км/год", is_correct=False)
        
        # Вопрос 48
        q = Question.objects.create(
            text="Чи дозволяється перевезення дітей до 12 років на передньому сидінні легкового автомобіля?",
            explanation="Перевезення дітей до 12 років на передньому сидінні легкового автомобіля дозволяється тільки з використанням спеціальних дитячих крісел."
        )
        questions_dict["b48"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="Не дозволяється в жодному випадку", is_correct=False)
        Answer.objects.create(question=q, text="Дозволяється тільки з використанням спеціальних дитячих крісел", is_correct=True)
        Answer.objects.create(question=q, text="Дозволяється без обмежень", is_correct=False)
        Answer.objects.create(question=q, text="Дозволяється тільки з використанням ременів безпеки", is_correct=False)
        
        # Вопрос 49
        q = Question.objects.create(
            text="Яка максимальна дозволена кількість пасажирів у легковому автомобілі?",
            explanation="Максимальна дозволена кількість пасажирів у легковому автомобілі визначається кількістю місць для сидіння."
        )
        questions_dict["b49"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="1 пасажир", is_correct=False)
        Answer.objects.create(question=q, text="2 пасажири", is_correct=False)
        Answer.objects.create(question=q, text="5 пасажирів", is_correct=False)
        Answer.objects.create(question=q, text="Максимальна кількість, яка дозволена законодавством", is_correct=True)
        
        # Вопрос 50
        q = Question.objects.create(
            text="Яка максимальна дозволена швидкість на дорогах за межами населених пунктів для легкових автомобілів?",
            explanation="На дорогах за межами населених пунктів для легкових автомобілів встановлено обмеження швидкості 90 км/год."
        )
        questions_dict["b50"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="70 км/год", is_correct=False)
        Answer.objects.create(question=q, text="90 км/год", is_correct=True)
        Answer.objects.create(question=q, text="110 км/год", is_correct=False)
        Answer.objects.create(question=q, text="130 км/год", is_correct=False)
        
        # Вопрос 51
        q = Question.objects.create(
            text="Як правильно розташовувати руки на кермі автомобіля?",
            explanation="Руки на кермі автомобіля повинні бути розташовані в положенні '10-2' або '9-3'."
        )
        questions_dict["b51"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="В положенні '12-6'", is_correct=False)
        Answer.objects.create(question=q, text="В положенні '10-2' або '9-3'", is_correct=True)
        Answer.objects.create(question=q, text="В положенні '8-4'", is_correct=False)
        Answer.objects.create(question=q, text="В будь-якому зручному положенні", is_correct=False)
        
        # Вопрос 52
        q = Question.objects.create(
            text="Чи дозволяється рух заднім ходом на автомагістралях?",
            explanation="Рух заднім ходом на автомагістралях заборонено."
        )
        questions_dict["b52"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="Так, це дозволено", is_correct=False)
        Answer.objects.create(question=q, text="Так, але тільки в крайній правій смузі", is_correct=False)
        Answer.objects.create(question=q, text="Ні, це заборонено", is_correct=True)
        Answer.objects.create(question=q, text="Так, але тільки в разі необхідності", is_correct=False)
        
        # Вопрос 53
        q = Question.objects.create(
            text="Яка максимальна дозволена швидкість у житлових зонах?",
            explanation="У житлових зонах максимальна дозволена швидкість становить 20 км/год."
        )
        questions_dict["b53"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="20 км/год", is_correct=True)
        Answer.objects.create(question=q, text="30 км/год", is_correct=False)
        Answer.objects.create(question=q, text="40 км/год", is_correct=False)
        Answer.objects.create(question=q, text="50 км/год", is_correct=False)
        
        # Вопрос 54
        q = Question.objects.create(
            text="Чи дозволяється перевезення дітей до 12 років на передньому сидінні легкового автомобіля?",
            explanation="Перевезення дітей до 12 років на передньому сидінні легкового автомобіля дозволяється тільки з використанням спеціальних дитячих крісел."
        )
        questions_dict["b54"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="Не дозволяється в жодному випадку", is_correct=False)
        Answer.objects.create(question=q, text="Дозволяється тільки з використанням спеціальних дитячих крісел", is_correct=True)
        Answer.objects.create(question=q, text="Дозволяється без обмежень", is_correct=False)
        Answer.objects.create(question=q, text="Дозволяється тільки з використанням ременів безпеки", is_correct=False)
        
        # Вопрос 55
        q = Question.objects.create(
            text="Яка максимальна дозволена кількість пасажирів у легковому автомобілі?",
            explanation="Максимальна дозволена кількість пасажирів у легковому автомобілі визначається кількістю місць для сидіння."
        )
        questions_dict["b55"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="1 пасажир", is_correct=False)
        Answer.objects.create(question=q, text="2 пасажири", is_correct=False)
        Answer.objects.create(question=q, text="5 пасажирів", is_correct=False)
        Answer.objects.create(question=q, text="Максимальна кількість, яка дозволена законодавством", is_correct=True)
        
        # Вопрос 56
        q = Question.objects.create(
            text="Яка максимальна дозволена швидкість на дорогах за межами населених пунктів для легкових автомобілів?",
            explanation="На дорогах за межами населених пунктів для легкових автомобілів встановлено обмеження швидкості 90 км/год."
        )
        questions_dict["b56"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="70 км/год", is_correct=False)
        Answer.objects.create(question=q, text="90 км/год", is_correct=True)
        Answer.objects.create(question=q, text="110 км/год", is_correct=False)
        Answer.objects.create(question=q, text="130 км/год", is_correct=False)
        
        # Вопрос 57
        q = Question.objects.create(
            text="Як правильно розташовувати руки на кермі автомобіля?",
            explanation="Руки на кермі автомобіля повинні бути розташовані в положенні '10-2' або '9-3'."
        )
        questions_dict["b57"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="В положенні '12-6'", is_correct=False)
        Answer.objects.create(question=q, text="В положенні '10-2' або '9-3'", is_correct=True)
        Answer.objects.create(question=q, text="В положенні '8-4'", is_correct=False)
        Answer.objects.create(question=q, text="В будь-якому зручному положенні", is_correct=False)
        
        # Вопрос 58
        q = Question.objects.create(
            text="Чи дозволяється рух заднім ходом на автомагістралях?",
            explanation="Рух заднім ходом на автомагістралях заборонено."
        )
        questions_dict["b58"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="Так, це дозволено", is_correct=False)
        Answer.objects.create(question=q, text="Так, але тільки в крайній правій смузі", is_correct=False)
        Answer.objects.create(question=q, text="Ні, це заборонено", is_correct=True)
        Answer.objects.create(question=q, text="Так, але тільки в разі необхідності", is_correct=False)
        
        # Вопрос 59
        q = Question.objects.create(
            text="Яка максимальна дозволена швидкість у житлових зонах?",
            explanation="У житлових зонах максимальна дозволена швидкість становить 20 км/год."
        )
        questions_dict["b59"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="20 км/год", is_correct=True)
        Answer.objects.create(question=q, text="30 км/год", is_correct=False)
        Answer.objects.create(question=q, text="40 км/год", is_correct=False)
        Answer.objects.create(question=q, text="50 км/год", is_correct=False)
        
        # Вопрос 60
        q = Question.objects.create(
            text="Чи дозволяється перевезення дітей до 12 років на передньому сидінні легкового автомобіля?",
            explanation="Перевезення дітей до 12 років на передньому сидінні легкового автомобіля дозволяється тільки з використанням спеціальних дитячих крісел."
        )
        questions_dict["b60"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="Не дозволяється в жодному випадку", is_correct=False)
        Answer.objects.create(question=q, text="Дозволяється тільки з використанням спеціальних дитячих крісел", is_correct=True)
        Answer.objects.create(question=q, text="Дозволяється без обмежень", is_correct=False)
        Answer.objects.create(question=q, text="Дозволяється тільки з використанням ременів безпеки", is_correct=False)
        
        # Вопрос 61
        q = Question.objects.create(
            text="Яка максимальна дозволена кількість пасажирів у легковому автомобілі?",
            explanation="Максимальна дозволена кількість пасажирів у легковому автомобілі визначається кількістю місць для сидіння."
        )
        questions_dict["b61"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="1 пасажир", is_correct=False)
        Answer.objects.create(question=q, text="2 пасажири", is_correct=False)
        Answer.objects.create(question=q, text="5 пасажирів", is_correct=False)
        Answer.objects.create(question=q, text="Максимальна кількість, яка дозволена законодавством", is_correct=True)
        
        # Вопрос 62
        q = Question.objects.create(
            text="Яка максимальна дозволена швидкість на дорогах за межами населених пунктів для легкових автомобілів?",
            explanation="На дорогах за межами населених пунктів для легкових автомобілів встановлено обмеження швидкості 90 км/год."
        )
        questions_dict["b62"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="70 км/год", is_correct=False)
        Answer.objects.create(question=q, text="90 км/год", is_correct=True)
        Answer.objects.create(question=q, text="110 км/год", is_correct=False)
        Answer.objects.create(question=q, text="130 км/год", is_correct=False)
        
        # Вопрос 63
        q = Question.objects.create(
            text="Як правильно розташовувати руки на кермі автомобіля?",
            explanation="Руки на кермі автомобіля повинні бути розташовані в положенні '10-2' або '9-3'."
        )
        questions_dict["b63"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="В положенні '12-6'", is_correct=False)
        Answer.objects.create(question=q, text="В положенні '10-2' або '9-3'", is_correct=True)
        Answer.objects.create(question=q, text="В положенні '8-4'", is_correct=False)
        Answer.objects.create(question=q, text="В будь-якому зручному положенні", is_correct=False)
        
        # Вопрос 64
        q = Question.objects.create(
            text="Чи дозволяється рух заднім ходом на автомагістралях?",
            explanation="Рух заднім ходом на автомагістралях заборонено."
        )
        questions_dict["b64"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="Так, це дозволено", is_correct=False)
        Answer.objects.create(question=q, text="Так, але тільки в крайній правій смузі", is_correct=False)
        Answer.objects.create(question=q, text="Ні, це заборонено", is_correct=True)
        Answer.objects.create(question=q, text="Так, але тільки в разі необхідності", is_correct=False)
        
        # Вопрос 65
        q = Question.objects.create(
            text="Яка максимальна дозволена швидкість у житлових зонах?",
            explanation="У житлових зонах максимальна дозволена швидкість становить 20 км/год."
        )
        questions_dict["b65"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="20 км/год", is_correct=True)
        Answer.objects.create(question=q, text="30 км/год", is_correct=False)
        Answer.objects.create(question=q, text="40 км/год", is_correct=False)
        Answer.objects.create(question=q, text="50 км/год", is_correct=False)
        
        # Вопрос 66
        q = Question.objects.create(
            text="Чи дозволяється перевезення дітей до 12 років на передньому сидінні легкового автомобіля?",
            explanation="Перевезення дітей до 12 років на передньому сидінні легкового автомобіля дозволяється тільки з використанням спеціальних дитячих крісел."
        )
        questions_dict["b66"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="Не дозволяється в жодному випадку", is_correct=False)
        Answer.objects.create(question=q, text="Дозволяється тільки з використанням спеціальних дитячих крісел", is_correct=True)
        Answer.objects.create(question=q, text="Дозволяється без обмежень", is_correct=False)
        Answer.objects.create(question=q, text="Дозволяється тільки з використанням ременів безпеки", is_correct=False)
        
        # Вопрос 67
        q = Question.objects.create(
            text="Яка максимальна дозволена кількість пасажирів у легковому автомобілі?",
            explanation="Максимальна дозволена кількість пасажирів у легковому автомобілі визначається кількістю місць для сидіння."
        )
        questions_dict["b67"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="1 пасажир", is_correct=False)
        Answer.objects.create(question=q, text="2 пасажири", is_correct=False)
        Answer.objects.create(question=q, text="5 пасажирів", is_correct=False)
        Answer.objects.create(question=q, text="Максимальна кількість, яка дозволена законодавством", is_correct=True)
        
        # Вопрос 68
        q = Question.objects.create(
            text="Яка максимальна дозволена швидкість на дорогах за межами населених пунктів для легкових автомобілів?",
            explanation="На дорогах за межами населених пунктів для легкових автомобілів встановлено обмеження швидкості 90 км/год."
        )
        questions_dict["b68"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="70 км/год", is_correct=False)
        Answer.objects.create(question=q, text="90 км/год", is_correct=True)
        Answer.objects.create(question=q, text="110 км/год", is_correct=False)
        Answer.objects.create(question=q, text="130 км/год", is_correct=False)
        
        # Вопрос 69
        q = Question.objects.create(
            text="Як правильно розташовувати руки на кермі автомобіля?",
            explanation="Руки на кермі автомобіля повинні бути розташовані в положенні '10-2' або '9-3'."
        )
        questions_dict["b69"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="В положенні '12-6'", is_correct=False)
        Answer.objects.create(question=q, text="В положенні '10-2' або '9-3'", is_correct=True)
        Answer.objects.create(question=q, text="В положенні '8-4'", is_correct=False)
        Answer.objects.create(question=q, text="В будь-якому зручному положенні", is_correct=False)
        
        # Вопрос 70
        q = Question.objects.create(
            text="Чи дозволяється рух заднім ходом на автомагістралях?",
            explanation="Рух заднім ходом на автомагістралях заборонено."
        )
        questions_dict["b70"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="Так, це дозволено", is_correct=False)
        Answer.objects.create(question=q, text="Так, але тільки в крайній правій смузі", is_correct=False)
        Answer.objects.create(question=q, text="Ні, це заборонено", is_correct=True)
        Answer.objects.create(question=q, text="Так, але тільки в разі необхідності", is_correct=False)
        
        # Вопрос 71
        q = Question.objects.create(
            text="Яка максимальна дозволена швидкість у житлових зонах?",
            explanation="У житлових зонах максимальна дозволена швидкість становить 20 км/год."
        )
        questions_dict["b71"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="20 км/год", is_correct=True)
        Answer.objects.create(question=q, text="30 км/год", is_correct=False)
        Answer.objects.create(question=q, text="40 км/год", is_correct=False)
        Answer.objects.create(question=q, text="50 км/год", is_correct=False)
        
        # Вопрос 72
        q = Question.objects.create(
            text="Чи дозволяється перевезення дітей до 12 років на передньому сидінні легкового автомобіля?",
            explanation="Перевезення дітей до 12 років на передньому сидінні легкового автомобіля дозволяється тільки з використанням спеціальних дитячих крісел."
        )
        questions_dict["b72"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="Не дозволяється в жодному випадку", is_correct=False)
        Answer.objects.create(question=q, text="Дозволяється тільки з використанням спеціальних дитячих крісел", is_correct=True)
        Answer.objects.create(question=q, text="Дозволяється без обмежень", is_correct=False)
        Answer.objects.create(question=q, text="Дозволяється тільки з використанням ременів безпеки", is_correct=False)
        
        # Вопрос 73
        q = Question.objects.create(
            text="Яка максимальна дозволена кількість пасажирів у легковому автомобілі?",
            explanation="Максимальна дозволена кількість пасажирів у легковому автомобілі визначається кількістю місць для сидіння."
        )
        questions_dict["b73"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="1 пасажир", is_correct=False)
        Answer.objects.create(question=q, text="2 пасажири", is_correct=False)
        Answer.objects.create(question=q, text="5 пасажирів", is_correct=False)
        Answer.objects.create(question=q, text="Максимальна кількість, яка дозволена законодавством", is_correct=True)
        
        # Вопрос 74
        q = Question.objects.create(
            text="Яка максимальна дозволена швидкість на дорогах за межами населених пунктів для легкових автомобілів?",
            explanation="На дорогах за межами населених пунктів для легкових автомобілів встановлено обмеження швидкості 90 км/год."
        )
        questions_dict["b74"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="70 км/год", is_correct=False)
        Answer.objects.create(question=q, text="90 км/год", is_correct=True)
        Answer.objects.create(question=q, text="110 км/год", is_correct=False)
        Answer.objects.create(question=q, text="130 км/год", is_correct=False)
        
        # Вопрос 75
        q = Question.objects.create(
            text="Як правильно розташовувати руки на кермі автомобіля?",
            explanation="Руки на кермі автомобіля повинні бути розташовані в положенні '10-2' або '9-3'."
        )
        questions_dict["b75"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="В положенні '12-6'", is_correct=False)
        Answer.objects.create(question=q, text="В положенні '10-2' або '9-3'", is_correct=True)
        Answer.objects.create(question=q, text="В положенні '8-4'", is_correct=False)
        Answer.objects.create(question=q, text="В будь-якому зручному положенні", is_correct=False)
        
        # Вопрос 76
        q = Question.objects.create(
            text="Чи дозволяється рух заднім ходом на автомагістралях?",
            explanation="Рух заднім ходом на автомагістралях заборонено."
        )
        questions_dict["b76"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="Так, це дозволено", is_correct=False)
        Answer.objects.create(question=q, text="Так, але тільки в крайній правій смузі", is_correct=False)
        Answer.objects.create(question=q, text="Ні, це заборонено", is_correct=True)
        Answer.objects.create(question=q, text="Так, але тільки в разі необхідності", is_correct=False)
        
        # Вопрос 77
        q = Question.objects.create(
            text="Яка максимальна дозволена швидкість у житлових зонах?",
            explanation="У житлових зонах максимальна дозволена швидкість становить 20 км/год."
        )
        questions_dict["b77"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="20 км/год", is_correct=True)
        Answer.objects.create(question=q, text="30 км/год", is_correct=False)
        Answer.objects.create(question=q, text="40 км/год", is_correct=False)
        Answer.objects.create(question=q, text="50 км/год", is_correct=False)
        
        # Вопрос 78
        q = Question.objects.create(
            text="Чи дозволяється перевезення дітей до 12 років на передньому сидінні легкового автомобіля?",
            explanation="Перевезення дітей до 12 років на передньому сидінні легкового автомобіля дозволяється тільки з використанням спеціальних дитячих крісел."
        )
        questions_dict["b78"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="Не дозволяється в жодному випадку", is_correct=False)
        Answer.objects.create(question=q, text="Дозволяється тільки з використанням спеціальних дитячих крісел", is_correct=True)
        Answer.objects.create(question=q, text="Дозволяється без обмежень", is_correct=False)
        Answer.objects.create(question=q, text="Дозволяється тільки з використанням ременів безпеки", is_correct=False)
        
        # Вопрос 79
        q = Question.objects.create(
            text="Яка максимальна дозволена кількість пасажирів у легковому автомобілі?",
            explanation="Максимальна дозволена кількість пасажирів у легковому автомобілі визначається кількістю місць для сидіння."
        )
        questions_dict["b79"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="1 пасажир", is_correct=False)
        Answer.objects.create(question=q, text="2 пасажири", is_correct=False)
        Answer.objects.create(question=q, text="5 пасажирів", is_correct=False)
        Answer.objects.create(question=q, text="Максимальна кількість, яка дозволена законодавством", is_correct=True)
        
        # Вопрос 80
        q = Question.objects.create(
            text="Яка максимальна дозволена швидкість на дорогах за межами населених пунктів для легкових автомобілів?",
            explanation="На дорогах за межами населених пунктів для легкових автомобілів встановлено обмеження швидкості 90 км/год."
        )
        questions_dict["b80"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="70 км/год", is_correct=False)
        Answer.objects.create(question=q, text="90 км/год", is_correct=True)
        Answer.objects.create(question=q, text="110 км/год", is_correct=False)
        Answer.objects.create(question=q, text="130 км/год", is_correct=False)
        
        # Вопрос 81
        q = Question.objects.create(
            text="Як правильно розташовувати руки на кермі автомобіля?",
            explanation="Руки на кермі автомобіля повинні бути розташовані в положенні '10-2' або '9-3'."
        )
        questions_dict["b81"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="В положенні '12-6'", is_correct=False)
        Answer.objects.create(question=q, text="В положенні '10-2' або '9-3'", is_correct=True)
        Answer.objects.create(question=q, text="В положенні '8-4'", is_correct=False)
        Answer.objects.create(question=q, text="В будь-якому зручному положенні", is_correct=False)
        
        # Вопрос 82
        q = Question.objects.create(
            text="Чи дозволяється рух заднім ходом на автомагістралях?",
            explanation="Рух заднім ходом на автомагістралях заборонено."
        )
        questions_dict["b82"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="Так, це дозволено", is_correct=False)
        Answer.objects.create(question=q, text="Так, але тільки в крайній правій смузі", is_correct=False)
        Answer.objects.create(question=q, text="Ні, це заборонено", is_correct=True)
        Answer.objects.create(question=q, text="Так, але тільки в разі необхідності", is_correct=False)
        
        # Вопрос 83
        q = Question.objects.create(
            text="Яка максимальна дозволена швидкість у житлових зонах?",
            explanation="У житлових зонах максимальна дозволена швидкість становить 20 км/год."
        )
        questions_dict["b83"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="20 км/год", is_correct=True)
        Answer.objects.create(question=q, text="30 км/год", is_correct=False)
        Answer.objects.create(question=q, text="40 км/год", is_correct=False)
        Answer.objects.create(question=q, text="50 км/год", is_correct=False)
        
        # Вопрос 84
        q = Question.objects.create(
            text="Чи дозволяється перевезення дітей до 12 років на передньому сидінні легкового автомобіля?",
            explanation="Перевезення дітей до 12 років на передньому сидінні легкового автомобіля дозволяється тільки з використанням спеціальних дитячих крісел."
        )
        questions_dict["b84"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="Не дозволяється в жодному випадку", is_correct=False)
        Answer.objects.create(question=q, text="Дозволяється тільки з використанням спеціальних дитячих крісел", is_correct=True)
        Answer.objects.create(question=q, text="Дозволяється без обмежень", is_correct=False)
        Answer.objects.create(question=q, text="Дозволяється тільки з використанням ременів безпеки", is_correct=False)
        
        # Вопрос 85
        q = Question.objects.create(
            text="Яка максимальна дозволена кількість пасажирів у легковому автомобілі?",
            explanation="Максимальна дозволена кількість пасажирів у легковому автомобілі визначається кількістю місць для сидіння."
        )
        questions_dict["b85"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="1 пасажир", is_correct=False)
        Answer.objects.create(question=q, text="2 пасажири", is_correct=False)
        Answer.objects.create(question=q, text="5 пасажирів", is_correct=False)
        Answer.objects.create(question=q, text="Максимальна кількість, яка дозволена законодавством", is_correct=True)
        
        # Вопрос 86
        q = Question.objects.create(
            text="Яка максимальна дозволена швидкість на дорогах за межами населених пунктів для легкових автомобілів?",
            explanation="На дорогах за межами населених пунктів для легкових автомобілів встановлено обмеження швидкості 90 км/год."
        )
        questions_dict["b86"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="70 км/год", is_correct=False)
        Answer.objects.create(question=q, text="90 км/год", is_correct=True)
        Answer.objects.create(question=q, text="110 км/год", is_correct=False)
        Answer.objects.create(question=q, text="130 км/год", is_correct=False)
        
        # Вопрос 87
        q = Question.objects.create(
            text="Як правильно розташовувати руки на кермі автомобіля?",
            explanation="Руки на кермі автомобіля повинні бути розташовані в положенні '10-2' або '9-3'."
        )
        questions_dict["b87"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="В положенні '12-6'", is_correct=False)
        Answer.objects.create(question=q, text="В положенні '10-2' або '9-3'", is_correct=True)
        Answer.objects.create(question=q, text="В положенні '8-4'", is_correct=False)
        Answer.objects.create(question=q, text="В будь-якому зручному положенні", is_correct=False)
        
        # Вопрос 88
        q = Question.objects.create(
            text="Чи дозволяється рух заднім ходом на автомагістралях?",
            explanation="Рух заднім ходом на автомагістралях заборонено."
        )
        questions_dict["b88"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="Так, це дозволено", is_correct=False)
        Answer.objects.create(question=q, text="Так, але тільки в крайній правій смузі", is_correct=False)
        Answer.objects.create(question=q, text="Ні, це заборонено", is_correct=True)
        Answer.objects.create(question=q, text="Так, але тільки в разі необхідності", is_correct=False)
        
        # Вопрос 89
        q = Question.objects.create(
            text="Яка максимальна дозволена швидкість у житлових зонах?",
            explanation="У житлових зонах максимальна дозволена швидкість становить 20 км/год."
        )
        questions_dict["b89"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="20 км/год", is_correct=True)
        Answer.objects.create(question=q, text="30 км/год", is_correct=False)
        Answer.objects.create(question=q, text="40 км/год", is_correct=False)
        Answer.objects.create(question=q, text="50 км/год", is_correct=False)
        
        # Вопрос 90
        q = Question.objects.create(
            text="Чи дозволяється перевезення дітей до 12 років на передньому сидінні легкового автомобіля?",
            explanation="Перевезення дітей до 12 років на передньому сидінні легкового автомобіля дозволяється тільки з використанням спеціальних дитячих крісел."
        )
        questions_dict["b90"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="Не дозволяється в жодному випадку", is_correct=False)
        Answer.objects.create(question=q, text="Дозволяється тільки з використанням спеціальних дитячих крісел", is_correct=True)
        Answer.objects.create(question=q, text="Дозволяється без обмежень", is_correct=False)
        Answer.objects.create(question=q, text="Дозволяється тільки з використанням ременів безпеки", is_correct=False)
        
        # Вопрос 91
        q = Question.objects.create(
            text="Яка максимальна дозволена кількість пасажирів у легковому автомобілі?",
            explanation="Максимальна дозволена кількість пасажирів у легковому автомобілі визначається кількістю місць для сидіння."
        )
        questions_dict["b91"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="1 пасажир", is_correct=False)
        Answer.objects.create(question=q, text="2 пасажири", is_correct=False)
        Answer.objects.create(question=q, text="5 пасажирів", is_correct=False)
        Answer.objects.create(question=q, text="Максимальна кількість, яка дозволена законодавством", is_correct=True)
        
        # Вопрос 92
        q = Question.objects.create(
            text="Яка максимальна дозволена швидкість на дорогах за межами населених пунктів для легкових автомобілів?",
            explanation="На дорогах за межами населених пунктів для легкових автомобілів встановлено обмеження швидкості 90 км/год."
        )
        questions_dict["b92"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="70 км/год", is_correct=False)
        Answer.objects.create(question=q, text="90 км/год", is_correct=True)
        Answer.objects.create(question=q, text="110 км/год", is_correct=False)
        Answer.objects.create(question=q, text="130 км/год", is_correct=False)
        
        # Вопрос 93
        q = Question.objects.create(
            text="Як правильно розташовувати руки на кермі автомобіля?",
            explanation="Руки на кермі автомобіля повинні бути розташовані в положенні '10-2' або '9-3'."
        )
        questions_dict["b93"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="В положенні '12-6'", is_correct=False)
        Answer.objects.create(question=q, text="В положенні '10-2' або '9-3'", is_correct=True)
        Answer.objects.create(question=q, text="В положенні '8-4'", is_correct=False)
        Answer.objects.create(question=q, text="В будь-якому зручному положенні", is_correct=False)
        
        # Вопрос 94
        q = Question.objects.create(
            text="Чи дозволяється рух заднім ходом на автомагістралях?",
            explanation="Рух заднім ходом на автомагістралях заборонено."
        )
        questions_dict["b94"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="Так, це дозволено", is_correct=False)
        Answer.objects.create(question=q, text="Так, але тільки в крайній правій смузі", is_correct=False)
        Answer.objects.create(question=q, text="Ні, це заборонено", is_correct=True)
        Answer.objects.create(question=q, text="Так, але тільки в разі необхідності", is_correct=False)
        
        # Вопрос 95
        q = Question.objects.create(
            text="Яка максимальна дозволена швидкість у житлових зонах?",
            explanation="У житлових зонах максимальна дозволена швидкість становить 20 км/год."
        )
        questions_dict["b95"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="20 км/год", is_correct=True)
        Answer.objects.create(question=q, text="30 км/год", is_correct=False)
        Answer.objects.create(question=q, text="40 км/год", is_correct=False)
        Answer.objects.create(question=q, text="50 км/год", is_correct=False)
        
        # Вопрос 96
        q = Question.objects.create(
            text="Чи дозволяється перевезення дітей до 12 років на передньому сидінні легкового автомобіля?",
            explanation="Перевезення дітей до 12 років на передньому сидінні легкового автомобіля дозволяється тільки з використанням спеціальних дитячих крісел."
        )
        questions_dict["b96"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="Не дозволяється в жодному випадку", is_correct=False)
        Answer.objects.create(question=q, text="Дозволяється тільки з використанням спеціальних дитячих крісел", is_correct=True)
        Answer.objects.create(question=q, text="Дозволяється без обмежень", is_correct=False)
        Answer.objects.create(question=q, text="Дозволяється тільки з використанням ременів безпеки", is_correct=False)
        
        # Вопрос 97
        q = Question.objects.create(
            text="Яка максимальна дозволена кількість пасажирів у легковому автомобілі?",
            explanation="Максимальна дозволена кількість пасажирів у легковому автомобілі визначається кількістю місць для сидіння."
        )
        questions_dict["b97"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="1 пасажир", is_correct=False)
        Answer.objects.create(question=q, text="2 пасажири", is_correct=False)
        Answer.objects.create(question=q, text="5 пасажирів", is_correct=False)
        Answer.objects.create(question=q, text="Максимальна кількість, яка дозволена законодавством", is_correct=True)
        
        # Вопрос 98
        q = Question.objects.create(
            text="Яка максимальна дозволена швидкість на дорогах за межами населених пунктів для легкових автомобілів?",
            explanation="На дорогах за межами населених пунктів для легкових автомобілів встановлено обмеження швидкості 90 км/год."
        )
        questions_dict["b98"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="70 км/год", is_correct=False)
        Answer.objects.create(question=q, text="90 км/год", is_correct=True)
        Answer.objects.create(question=q, text="110 км/год", is_correct=False)
        Answer.objects.create(question=q, text="130 км/год", is_correct=False)
        
        # Вопрос 99
        q = Question.objects.create(
            text="Як правильно розташовувати руки на кермі автомобіля?",
            explanation="Руки на кермі автомобіля повинні бути розташовані в положенні '10-2' або '9-3'."
        )
        questions_dict["b99"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="В положенні '12-6'", is_correct=False)
        Answer.objects.create(question=q, text="В положенні '10-2' або '9-3'", is_correct=True)
        Answer.objects.create(question=q, text="В положенні '8-4'", is_correct=False)
        Answer.objects.create(question=q, text="В будь-якому зручному положенні", is_correct=False)
        
        # Вопрос 100
        q = Question.objects.create(
            text="Чи дозволяється рух заднім ходом на автомагістралях?",
            explanation="Рух заднім ходом на автомагістралях заборонено."
        )
        questions_dict["b100"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="Так, це дозволено", is_correct=False)
        Answer.objects.create(question=q, text="Так, але тільки в крайній правій смузі", is_correct=False)
        Answer.objects.create(question=q, text="Ні, це заборонено", is_correct=True)
        Answer.objects.create(question=q, text="Так, але тільки в разі необхідності", is_correct=False)
        
        # Вопрос 101
        q = Question.objects.create(
            text="Яка максимальна дозволена швидкість у житлових зонах?",
            explanation="У житлових зонах максимальна дозволена швидкість становить 20 км/год."
        )
        questions_dict["b101"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="20 км/год", is_correct=True)
        Answer.objects.create(question=q, text="30 км/год", is_correct=False)
        Answer.objects.create(question=q, text="40 км/год", is_correct=False)
        Answer.objects.create(question=q, text="50 км/год", is_correct=False)
        
        # Вопрос 102
        q = Question.objects.create(
            text="Чи дозволяється перевезення дітей до 12 років на передньому сидінні легкового автомобіля?",
            explanation="Перевезення дітей до 12 років на передньому сидінні легкового автомобіля дозволяється тільки з використанням спеціальних дитячих крісел."
        )
        questions_dict["b102"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="Не дозволяється в жодному випадку", is_correct=False)
        Answer.objects.create(question=q, text="Дозволяється тільки з використанням спеціальних дитячих крісел", is_correct=True)
        Answer.objects.create(question=q, text="Дозволяється без обмежень", is_correct=False)
        Answer.objects.create(question=q, text="Дозволяється тільки з використанням ременів безпеки", is_correct=False)
        
        # Вопрос 103
        q = Question.objects.create(
            text="Яка максимальна дозволена кількість пасажирів у легковому автомобілі?",
            explanation="Максимальна дозволена кількість пасажирів у легковому автомобілі визначається кількістю місць для сидіння."
        )
        questions_dict["b103"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="1 пасажир", is_correct=False)
        Answer.objects.create(question=q, text="2 пасажири", is_correct=False)
        Answer.objects.create(question=q, text="5 пасажирів", is_correct=False)
        Answer.objects.create(question=q, text="Максимальна кількість, яка дозволена законодавством", is_correct=True)
        
        # Вопрос 104
        q = Question.objects.create(
            text="Яка максимальна дозволена швидкість на дорогах за межами населених пунктів для легкових автомобілів?",
            explanation="На дорогах за межами населених пунктів для легкових автомобілів встановлено обмеження швидкості 90 км/год."
        )
        questions_dict["b104"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="70 км/год", is_correct=False)
        Answer.objects.create(question=q, text="90 км/год", is_correct=True)
        Answer.objects.create(question=q, text="110 км/год", is_correct=False)
        Answer.objects.create(question=q, text="130 км/год", is_correct=False)
        
        # Вопрос 105
        q = Question.objects.create(
            text="Як правильно розташовувати руки на кермі автомобіля?",
            explanation="Руки на кермі автомобіля повинні бути розташовані в положенні '10-2' або '9-3'."
        )
        questions_dict["b105"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="В положенні '12-6'", is_correct=False)
        Answer.objects.create(question=q, text="В положенні '10-2' або '9-3'", is_correct=True)
        Answer.objects.create(question=q, text="В положенні '8-4'", is_correct=False)
        Answer.objects.create(question=q, text="В будь-якому зручному положенні", is_correct=False)
        
        # Вопрос 106
        q = Question.objects.create(
            text="Чи дозволяється рух заднім ходом на автомагістралях?",
            explanation="Рух заднім ходом на автомагістралях заборонено."
        )
        questions_dict["b106"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="Так, це дозволено", is_correct=False)
        Answer.objects.create(question=q, text="Так, але тільки в крайній правій смузі", is_correct=False)
        Answer.objects.create(question=q, text="Ні, це заборонено", is_correct=True)
        Answer.objects.create(question=q, text="Так, але тільки в разі необхідності", is_correct=False)
        
        # Вопрос 107
        q = Question.objects.create(
            text="Яка максимальна дозволена швидкість у житлових зонах?",
            explanation="У житлових зонах максимальна дозволена швидкість становить 20 км/год."
        )
        questions_dict["b107"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="20 км/год", is_correct=True)
        Answer.objects.create(question=q, text="30 км/год", is_correct=False)
        Answer.objects.create(question=q, text="40 км/год", is_correct=False)
        Answer.objects.create(question=q, text="50 км/год", is_correct=False)
        
        # Вопрос 108
        q = Question.objects.create(
            text="Чи дозволяється перевезення дітей до 12 років на передньому сидінні легкового автомобіля?",
            explanation="Перевезення дітей до 12 років на передньому сидінні легкового автомобіля дозволяється тільки з використанням спеціальних дитячих крісел."
        )
        questions_dict["b108"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="Не дозволяється в жодному випадку", is_correct=False)
        Answer.objects.create(question=q, text="Дозволяється тільки з використанням спеціальних дитячих крісел", is_correct=True)
        Answer.objects.create(question=q, text="Дозволяється без обмежень", is_correct=False)
        Answer.objects.create(question=q, text="Дозволяється тільки з використанням ременів безпеки", is_correct=False)
        
        # Вопрос 109
        q = Question.objects.create(
            text="Яка максимальна дозволена кількість пасажирів у легковому автомобілі?",
            explanation="Максимальна дозволена кількість пасажирів у легковому автомобілі визначається кількістю місць для сидіння."
        )
        questions_dict["b109"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="1 пасажир", is_correct=False)
        Answer.objects.create(question=q, text="2 пасажири", is_correct=False)
        Answer.objects.create(question=q, text="5 пасажирів", is_correct=False)
        Answer.objects.create(question=q, text="Максимальна кількість, яка дозволена законодавством", is_correct=True)
        
        # Вопрос 110
        q = Question.objects.create(
            text="Яка максимальна дозволена швидкість на дорогах за межами населених пунктів для легкових автомобілів?",
            explanation="На дорогах за межами населених пунктів для легкових автомобілів встановлено обмеження швидкості 90 км/год."
        )
        questions_dict["b110"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="70 км/год", is_correct=False)
        Answer.objects.create(question=q, text="90 км/год", is_correct=True)
        Answer.objects.create(question=q, text="110 км/год", is_correct=False)
        Answer.objects.create(question=q, text="130 км/год", is_correct=False)
        
        # Вопрос 111
        q = Question.objects.create(
            text="Як правильно розташовувати руки на кермі автомобіля?",
            explanation="Руки на кермі автомобіля повинні бути розташовані в положенні '10-2' або '9-3'."
        )
        questions_dict["b111"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="В положенні '12-6'", is_correct=False)
        Answer.objects.create(question=q, text="В положенні '10-2' або '9-3'", is_correct=True)
        Answer.objects.create(question=q, text="В положенні '8-4'", is_correct=False)
        Answer.objects.create(question=q, text="В будь-якому зручному положенні", is_correct=False)
        
        # Вопрос 112
        q = Question.objects.create(
            text="Чи дозволяється рух заднім ходом на автомагістралях?",
            explanation="Рух заднім ходом на автомагістралях заборонено."
        )
        questions_dict["b112"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="Так, це дозволено", is_correct=False)
        Answer.objects.create(question=q, text="Так, але тільки в крайній правій смузі", is_correct=False)
        Answer.objects.create(question=q, text="Ні, це заборонено", is_correct=True)
        Answer.objects.create(question=q, text="Так, але тільки в разі необхідності", is_correct=False)
        
        # Вопрос 113
        q = Question.objects.create(
            text="Яка максимальна дозволена швидкість у житлових зонах?",
            explanation="У житлових зонах максимальна дозволена швидкість становить 20 км/год."
        )
        questions_dict["b113"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="20 км/год", is_correct=True)
        Answer.objects.create(question=q, text="30 км/год", is_correct=False)
        Answer.objects.create(question=q, text="40 км/год", is_correct=False)
        Answer.objects.create(question=q, text="50 км/год", is_correct=False)
        
        # Вопрос 114
        q = Question.objects.create(
            text="Чи дозволяється перевезення дітей до 12 років на передньому сидінні легкового автомобіля?",
            explanation="Перевезення дітей до 12 років на передньому сидінні легкового автомобіля дозволяється тільки з використанням спеціальних дитячих крісел."
        )
        questions_dict["b114"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="Не дозволяється в жодному випадку", is_correct=False)
        Answer.objects.create(question=q, text="Дозволяється тільки з використанням спеціальних дитячих крісел", is_correct=True)
        Answer.objects.create(question=q, text="Дозволяється без обмежень", is_correct=False)
        Answer.objects.create(question=q, text="Дозволяється тільки з використанням ременів безпеки", is_correct=False)
        
        # Вопрос 115
        q = Question.objects.create(
            text="Яка максимальна дозволена кількість пасажирів у легковому автомобілі?",
            explanation="Максимальна дозволена кількість пасажирів у легковому автомобілі визначається кількістю місць для сидіння."
        )
        questions_dict["b115"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="1 пасажир", is_correct=False)
        Answer.objects.create(question=q, text="2 пасажири", is_correct=False)
        Answer.objects.create(question=q, text="5 пасажирів", is_correct=False)
        Answer.objects.create(question=q, text="Максимальна кількість, яка дозволена законодавством", is_correct=True)
        
        # Вопрос 116
        q = Question.objects.create(
            text="Яка максимальна дозволена швидкість на дорогах за межами населених пунктів для легкових автомобілів?",
            explanation="На дорогах за межами населених пунктів для легкових автомобілів встановлено обмеження швидкості 90 км/год."
        )
        questions_dict["b116"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="70 км/год", is_correct=False)
        Answer.objects.create(question=q, text="90 км/год", is_correct=True)
        Answer.objects.create(question=q, text="110 км/год", is_correct=False)
        Answer.objects.create(question=q, text="130 км/год", is_correct=False)
        
        # Вопрос 117
        q = Question.objects.create(
            text="Як правильно розташовувати руки на кермі автомобіля?",
            explanation="Руки на кермі автомобіля повинні бути розташовані в положенні '10-2' або '9-3'."
        )
        questions_dict["b117"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="В положенні '12-6'", is_correct=False)
        Answer.objects.create(question=q, text="В положенні '10-2' або '9-3'", is_correct=True)
        Answer.objects.create(question=q, text="В положенні '8-4'", is_correct=False)
        Answer.objects.create(question=q, text="В будь-якому зручному положенні", is_correct=False)
        
        # Вопрос 118
        q = Question.objects.create(
            text="Чи дозволяється рух заднім ходом на автомагістралях?",
            explanation="Рух заднім ходом на автомагістралях заборонено."
        )
        questions_dict["b118"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="Так, це дозволено", is_correct=False)
        Answer.objects.create(question=q, text="Так, але тільки в крайній правій смузі", is_correct=False)
        Answer.objects.create(question=q, text="Ні, це заборонено", is_correct=True)
        Answer.objects.create(question=q, text="Так, але тільки в разі необхідності", is_correct=False)
        
        # Вопрос 119
        q = Question.objects.create(
            text="Яка максимальна дозволена швидкість у житлових зонах?",
            explanation="У житлових зонах максимальна дозволена швидкість становить 20 км/год."
        )
        questions_dict["b119"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="20 км/год", is_correct=True)
        Answer.objects.create(question=q, text="30 км/год", is_correct=False)
        Answer.objects.create(question=q, text="40 км/год", is_correct=False)
        Answer.objects.create(question=q, text="50 км/год", is_correct=False)
        
        # Вопрос 120
        q = Question.objects.create(
            text="Чи дозволяється перевезення дітей до 12 років на передньому сидінні легкового автомобіля?",
            explanation="Перевезення дітей до 12 років на передньому сидінні легкового автомобіля дозволяється тільки з використанням спеціальних дитячих крісел."
        )
        questions_dict["b120"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="Не дозволяється в жодному випадку", is_correct=False)
        Answer.objects.create(question=q, text="Дозволяється тільки з використанням спеціальних дитячих крісел", is_correct=True)
        Answer.objects.create(question=q, text="Дозволяється без обмежень", is_correct=False)
        Answer.objects.create(question=q, text="Дозволяється тільки з використанням ременів безпеки", is_correct=False)
        
        # Вопрос 121
        q = Question.objects.create(
            text="Яка максимальна дозволена кількість пасажирів у легковому автомобілі?",
            explanation="Максимальна дозволена кількість пасажирів у легковому автомобілі визначається кількістю місць для сидіння."
        )
        questions_dict["b121"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="1 пасажир", is_correct=False)
        Answer.objects.create(question=q, text="2 пасажири", is_correct=False)
        Answer.objects.create(question=q, text="5 пасажирів", is_correct=False)
        Answer.objects.create(question=q, text="Максимальна кількість, яка дозволена законодавством", is_correct=True)
        
        # Вопрос 122
        q = Question.objects.create(
            text="Яка максимальна дозволена швидкість на дорогах за межами населених пунктів для легкових автомобілів?",
            explanation="На дорогах за межами населених пунктів для легкових автомобілів встановлено обмеження швидкості 90 км/год."
        )
        questions_dict["b122"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="70 км/год", is_correct=False)
        Answer.objects.create(question=q, text="90 км/год", is_correct=True)
        Answer.objects.create(question=q, text="110 км/год", is_correct=False)
        Answer.objects.create(question=q, text="130 км/год", is_correct=False)
        
        # Вопрос 123
        q = Question.objects.create(
            text="Як правильно розташовувати руки на кермі автомобіля?",
            explanation="Руки на кермі автомобіля повинні бути розташовані в положенні '10-2' або '9-3'."
        )
        questions_dict["b123"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="В положенні '12-6'", is_correct=False)
        Answer.objects.create(question=q, text="В положенні '10-2' або '9-3'", is_correct=True)
        Answer.objects.create(question=q, text="В положенні '8-4'", is_correct=False)
        Answer.objects.create(question=q, text="В будь-якому зручному положенні", is_correct=False)
        
        # Вопрос 124
        q = Question.objects.create(
            text="Чи дозволяється рух заднім ходом на автомагістралях?",
            explanation="Рух заднім ходом на автомагістралях заборонено."
        )
        questions_dict["b124"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="Так, це дозволено", is_correct=False)
        Answer.objects.create(question=q, text="Так, але тільки в крайній правій смузі", is_correct=False)
        Answer.objects.create(question=q, text="Ні, це заборонено", is_correct=True)
        Answer.objects.create(question=q, text="Так, але тільки в разі необхідності", is_correct=False)
        
        # Вопрос 125
        q = Question.objects.create(
            text="Яка максимальна дозволена швидкість у житлових зонах?",
            explanation="У житлових зонах максимальна дозволена швидкість становить 20 км/год."
        )
        questions_dict["b125"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="20 км/год", is_correct=True)
        Answer.objects.create(question=q, text="30 км/год", is_correct=False)
        Answer.objects.create(question=q, text="40 км/год", is_correct=False)
        Answer.objects.create(question=q, text="50 км/год", is_correct=False)
        
        # Вопрос 126
        q = Question.objects.create(
            text="Чи дозволяється перевезення дітей до 12 років на передньому сидінні легкового автомобіля?",
            explanation="Перевезення дітей до 12 років на передньому сидінні легкового автомобіля дозволяється тільки з використанням спеціальних дитячих крісел."
        )
        questions_dict["b126"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="Не дозволяється в жодному випадку", is_correct=False)
        Answer.objects.create(question=q, text="Дозволяється тільки з використанням спеціальних дитячих крісел", is_correct=True)
        Answer.objects.create(question=q, text="Дозволяється без обмежень", is_correct=False)
        Answer.objects.create(question=q, text="Дозволяється тільки з використанням ременів безпеки", is_correct=False)
        
        # Вопрос 127
        q = Question.objects.create(
            text="Яка максимальна дозволена кількість пасажирів у легковому автомобілі?",
            explanation="Максимальна дозволена кількість пасажирів у легковому автомобілі визначається кількістю місць для сидіння."
        )
        questions_dict["b127"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="1 пасажир", is_correct=False)
        Answer.objects.create(question=q, text="2 пасажири", is_correct=False)
        Answer.objects.create(question=q, text="5 пасажирів", is_correct=False)
        Answer.objects.create(question=q, text="Максимальна кількість, яка дозволена законодавством", is_correct=True)
        
        # Вопрос 128
        q = Question.objects.create(
            text="Яка максимальна дозволена швидкість на дорогах за межами населених пунктів для легкових автомобілів?",
            explanation="На дорогах за межами населених пунктів для легкових автомобілів встановлено обмеження швидкості 90 км/год."
        )
        questions_dict["b128"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="70 км/год", is_correct=False)
        Answer.objects.create(question=q, text="90 км/год", is_correct=True)
        Answer.objects.create(question=q, text="110 км/год", is_correct=False)
        Answer.objects.create(question=q, text="130 км/год", is_correct=False)
        
        # Вопрос 129
        q = Question.objects.create(
            text="Як правильно розташовувати руки на кермі автомобіля?",
            explanation="Руки на кермі автомобіля повинні бути розташовані в положенні '10-2' або '9-3'."
        )
        questions_dict["b129"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="В положенні '12-6'", is_correct=False)
        Answer.objects.create(question=q, text="В положенні '10-2' або '9-3'", is_correct=True)
        Answer.objects.create(question=q, text="В положенні '8-4'", is_correct=False)
        Answer.objects.create(question=q, text="В будь-якому зручному положенні", is_correct=False)
        
        # Вопрос 130
        q = Question.objects.create(
            text="Чи дозволяється рух заднім ходом на автомагістралях?",
            explanation="Рух заднім ходом на автомагістралях заборонено."
        )
        questions_dict["b130"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="Так, це дозволено", is_correct=False)
        Answer.objects.create(question=q, text="Так, але тільки в крайній правій смузі", is_correct=False)
        Answer.objects.create(question=q, text="Ні, це заборонено", is_correct=True)
        Answer.objects.create(question=q, text="Так, але тільки в разі необхідності", is_correct=False)
        
        # Вопрос 131
        q = Question.objects.create(
            text="Яка максимальна дозволена швидкість у житлових зонах?",
            explanation="У житлових зонах максимальна дозволена швидкість становить 20 км/год."
        )
        questions_dict["b131"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="20 км/год", is_correct=True)
        Answer.objects.create(question=q, text="30 км/год", is_correct=False)
        Answer.objects.create(question=q, text="40 км/год", is_correct=False)
        Answer.objects.create(question=q, text="50 км/год", is_correct=False)
        
        # Вопрос 132
        q = Question.objects.create(
            text="Чи дозволяється перевезення дітей до 12 років на передньому сидінні легкового автомобіля?",
            explanation="Перевезення дітей до 12 років на передньому сидінні легкового автомобіля дозволяється тільки з використанням спеціальних дитячих крісел."
        )
        questions_dict["b132"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="Не дозволяється в жодному випадку", is_correct=False)
        Answer.objects.create(question=q, text="Дозволяється тільки з використанням спеціальних дитячих крісел", is_correct=True)
        Answer.objects.create(question=q, text="Дозволяється без обмежень", is_correct=False)
        Answer.objects.create(question=q, text="Дозволяється тільки з використанням ременів безпеки", is_correct=False)
        
        # Вопрос 133
        q = Question.objects.create(
            text="Яка максимальна дозволена кількість пасажирів у легковому автомобілі?",
            explanation="Максимальна дозволена кількість пасажирів у легковому автомобілі визначається кількістю місць для сидіння."
        )
        questions_dict["b133"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="1 пасажир", is_correct=False)
        Answer.objects.create(question=q, text="2 пасажири", is_correct=False)
        Answer.objects.create(question=q, text="5 пасажирів", is_correct=False)
        Answer.objects.create(question=q, text="Максимальна кількість, яка дозволена законодавством", is_correct=True)
        
        # Вопрос 134
        q = Question.objects.create(
            text="Яка максимальна дозволена швидкість на дорогах за межами населених пунктів для легкових автомобілів?",
            explanation="На дорогах за межами населених пунктів для легкових автомобілів встановлено обмеження швидкості 90 км/год."
        )
        questions_dict["b134"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="70 км/год", is_correct=False)
        Answer.objects.create(question=q, text="90 км/год", is_correct=True)
        Answer.objects.create(question=q, text="110 км/год", is_correct=False)
        Answer.objects.create(question=q, text="130 км/год", is_correct=False)
        
        # Вопрос 135
        q = Question.objects.create(
            text="Як правильно розташовувати руки на кермі автомобіля?",
            explanation="Руки на кермі автомобіля повинні бути розташовані в положенні '10-2' або '9-3'."
        )
        questions_dict["b135"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="В положенні '12-6'", is_correct=False)
        Answer.objects.create(question=q, text="В положенні '10-2' або '9-3'", is_correct=True)
        Answer.objects.create(question=q, text="В положенні '8-4'", is_correct=False)
        Answer.objects.create(question=q, text="В будь-якому зручному положенні", is_correct=False)
        
        # Вопрос 136
        q = Question.objects.create(
            text="Чи дозволяється рух заднім ходом на автомагістралях?",
            explanation="Рух заднім ходом на автомагістралях заборонено."
        )
        questions_dict["b136"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="Так, це дозволено", is_correct=False)
        Answer.objects.create(question=q, text="Так, але тільки в крайній правій смузі", is_correct=False)
        Answer.objects.create(question=q, text="Ні, це заборонено", is_correct=True)
        Answer.objects.create(question=q, text="Так, але тільки в разі необхідності", is_correct=False)
        
        # Вопрос 137
        q = Question.objects.create(
            text="Яка максимальна дозволена швидкість у житлових зонах?",
            explanation="У житлових зонах максимальна дозволена швидкість становить 20 км/год."
        )
        questions_dict["b137"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="20 км/год", is_correct=True)
        Answer.objects.create(question=q, text="30 км/год", is_correct=False)
        Answer.objects.create(question=q, text="40 км/год", is_correct=False)
        Answer.objects.create(question=q, text="50 км/год", is_correct=False)
        
        # Вопрос 138
        q = Question.objects.create(
            text="Чи дозволяється перевезення дітей до 12 років на передньому сидінні легкового автомобіля?",
            explanation="Перевезення дітей до 12 років на передньому сидінні легкового автомобіля дозволяється тільки з використанням спеціальних дитячих крісел."
        )
        questions_dict["b138"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="Не дозволяється в жодному випадку", is_correct=False)
        Answer.objects.create(question=q, text="Дозволяється тільки з використанням спеціальних дитячих крісел", is_correct=True)
        Answer.objects.create(question=q, text="Дозволяється без обмежень", is_correct=False)
        Answer.objects.create(question=q, text="Дозволяється тільки з використанням ременів безпеки", is_correct=False)
        
        # Вопрос 139
        q = Question.objects.create(
            text="Яка максимальна дозволена кількість пасажирів у легковому автомобілі?",
            explanation="Максимальна дозволена кількість пасажирів у легковому автомобілі визначається кількістю місць для сидіння."
        )
        questions_dict["b139"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="1 пасажир", is_correct=False)
        Answer.objects.create(question=q, text="2 пасажири", is_correct=False)
        Answer.objects.create(question=q, text="5 пасажирів", is_correct=False)
        Answer.objects.create(question=q, text="Максимальна кількість, яка дозволена законодавством", is_correct=True)
        
        # Вопрос 140
        q = Question.objects.create(
            text="Яка максимальна дозволена швидкість на дорогах за межами населених пунктів для легкових автомобілів?",
            explanation="На дорогах за межами населених пунктів для легкових автомобілів встановлено обмеження швидкості 90 км/год."
        )
        questions_dict["b140"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="70 км/год", is_correct=False)
        Answer.objects.create(question=q, text="90 км/год", is_correct=True)
        Answer.objects.create(question=q, text="110 км/год", is_correct=False)
        Answer.objects.create(question=q, text="130 км/год", is_correct=False)
        
        # Вопрос 141
        q = Question.objects.create(
            text="Як правильно розташовувати руки на кермі автомобіля?",
            explanation="Руки на кермі автомобіля повинні бути розташовані в положенні '10-2' або '9-3'."
        )
        questions_dict["b141"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="В положенні '12-6'", is_correct=False)
        Answer.objects.create(question=q, text="В положенні '10-2' або '9-3'", is_correct=True)
        Answer.objects.create(question=q, text="В положенні '8-4'", is_correct=False)
        Answer.objects.create(question=q, text="В будь-якому зручному положенні", is_correct=False)
        
        # Вопрос 142
        q = Question.objects.create(
            text="Чи дозволяється рух заднім ходом на автомагістралях?",
            explanation="Рух заднім ходом на автомагістралях заборонено."
        )
        questions_dict["b142"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="Так, це дозволено", is_correct=False)
        Answer.objects.create(question=q, text="Так, але тільки в крайній правій смузі", is_correct=False)
        Answer.objects.create(question=q, text="Ні, це заборонено", is_correct=True)
        Answer.objects.create(question=q, text="Так, але тільки в разі необхідності", is_correct=False)
        
        # Вопрос 143
        q = Question.objects.create(
            text="Яка максимальна дозволена швидкість у житлових зонах?",
            explanation="У житлових зонах максимальна дозволена швидкість становить 20 км/год."
        )
        questions_dict["b143"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="20 км/год", is_correct=True)
        Answer.objects.create(question=q, text="30 км/год", is_correct=False)
        Answer.objects.create(question=q, text="40 км/год", is_correct=False)
        Answer.objects.create(question=q, text="50 км/год", is_correct=False)
        
        # Вопрос 144
        q = Question.objects.create(
            text="Чи дозволяється перевезення дітей до 12 років на передньому сидінні легкового автомобіля?",
            explanation="Перевезення дітей до 12 років на передньому сидінні легкового автомобіля дозволяється тільки з використанням спеціальних дитячих крісел."
        )
        questions_dict["b144"] = q
        QuizzesQuestions.objects.create(quiz=quiz_b, question=q)
        
        Answer.objects.create(question=q, text="Не дозволяється в жодному випадку", is_correct=False)
        Answer.objects.create(question=q, text="Дозволяється тільки з використанням спеціальних дитячих крісел", is_correct=True)
        Answer.objects.create(question=q, text="Дозволяється без обмежень", is_correct=False)
        Answer.objects.create(question=q, text="Дозволяється тільки з використанням ременів безпеки", is_correct=False)
        
        print(f"Created {Quiz.objects.count()} quizzes")
        print(f"Created {Question.objects.count()} questions")
        print(f"Created {Answer.objects.count()} answers")
        
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
        
        return True
    except Exception as e:
        print(f"Error in create_extended_pdd_data: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Running extended_pdd_questions.py script")
    success = create_extended_pdd_data()
    sys.exit(0 if success else 1)
    