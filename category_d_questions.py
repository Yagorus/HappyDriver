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

def create_category_d_data():
    try:
        print("Creating questions for Category D (Автобусы)...")
        
        # Находим или создаем квиз для категории D
        quiz_d, created = Quiz.objects.get_or_create(
            category="D",
            defaults={
                "title": "Правила дорожнього руху - категорія D",
                "is_random": False
            }
        )
        
        if created:
            print(f"Created quiz D: {quiz_d.title}")
        else:
            print(f"Found existing quiz D: {quiz_d.title}")
            # Очищаем существующие вопросы для квиза
            QuizzesQuestions.objects.filter(quiz=quiz_d).delete()
            print("Cleared existing questions for Category D")
        
        # Создаем словарь для хранения созданных вопросов
        questions_dict = {}
        
        # Вопрос 1
        q = Question.objects.create(
            text="Який мінімальний вік водія для керування автобусом?",
            explanation="Для керування автобусом (категорія D) водій повинен досягти віку 21 рік."
        )
        questions_dict["d1"] = q
        QuizzesQuestions.objects.create(quiz=quiz_d, question=q)
        
        Answer.objects.create(question=q, text="18 років", is_correct=False)
        Answer.objects.create(question=q, text="19 років", is_correct=False)
        Answer.objects.create(question=q, text="21 рік", is_correct=True)
        Answer.objects.create(question=q, text="24 роки", is_correct=False)
        
        # Вопрос 2
        q = Question.objects.create(
            text="Яка максимальна швидкість руху автобусів у населених пунктах?",
            explanation="Максимальна швидкість руху автобусів у населених пунктах становить 50 км/год."
        )
        questions_dict["d2"] = q
        QuizzesQuestions.objects.create(quiz=quiz_d, question=q)
        
        Answer.objects.create(question=q, text="40 км/год", is_correct=False)
        Answer.objects.create(question=q, text="50 км/год", is_correct=True)
        Answer.objects.create(question=q, text="60 км/год", is_correct=False)
        Answer.objects.create(question=q, text="70 км/год", is_correct=False)
        
        # Вопрос 3
        q = Question.objects.create(
            text="На яку максимальну відстань може відхилятися автобус від краю проїзної частини під час посадки (висадки) пасажирів?",
            explanation="Автобус може відхилятися від краю проїзної частини під час посадки (висадки) пасажирів на відстань не більше 0,5 метра."
        )
        questions_dict["d3"] = q
        QuizzesQuestions.objects.create(quiz=quiz_d, question=q)
        
        Answer.objects.create(question=q, text="0,3 метра", is_correct=False)
        Answer.objects.create(question=q, text="0,5 метра", is_correct=True)
        Answer.objects.create(question=q, text="1 метр", is_correct=False)
        Answer.objects.create(question=q, text="1,5 метра", is_correct=False)
        
        # Вопрос 4
        q = Question.objects.create(
            text="Чи може водій автобуса під час руху розмовляти з пасажирами?",
            explanation="Водію автобуса заборонено під час руху розмовляти з пасажирами, вживати їжу, пити, курити."
        )
        questions_dict["d4"] = q
        QuizzesQuestions.objects.create(quiz=quiz_d, question=q)
        
        Answer.objects.create(question=q, text="Так, це дозволено", is_correct=False)
        Answer.objects.create(question=q, text="Ні, це заборонено", is_correct=True)
        Answer.objects.create(question=q, text="Дозволено тільки з пасажирами на передньому сидінні", is_correct=False)
        Answer.objects.create(question=q, text="Дозволено тільки через гучномовець", is_correct=False)
        
        # Вопрос 5
        q = Question.objects.create(
            text="Як часто водії автобусів повинні проходити медичний огляд?",
            explanation="Водії автобусів повинні проходити медичний огляд кожні 12 місяців."
        )
        questions_dict["d5"] = q
        QuizzesQuestions.objects.create(quiz=quiz_d, question=q)
        
        Answer.objects.create(question=q, text="Кожні 6 місяців", is_correct=False)
        Answer.objects.create(question=q, text="Кожні 12 місяців", is_correct=True)
        Answer.objects.create(question=q, text="Кожні 24 місяця", is_correct=False)
        Answer.objects.create(question=q, text="Кожні 36 місяців", is_correct=False)
        
        # Вопрос 6
        q = Question.objects.create(
            text="Яку мінімальну дистанцію повинні дотримуватися автобуси при русі в колоні?",
            explanation="При русі в колоні автобуси повинні дотримуватися мінімальної дистанції 80 метрів."
        )
        questions_dict["d6"] = q
        QuizzesQuestions.objects.create(quiz=quiz_d, question=q)
        
        Answer.objects.create(question=q, text="30 метрів", is_correct=False)
        Answer.objects.create(question=q, text="50 метрів", is_correct=False)
        Answer.objects.create(question=q, text="80 метрів", is_correct=True)
        Answer.objects.create(question=q, text="100 метрів", is_correct=False)
        
        # Вопрос 7
        q = Question.objects.create(
            text="Чи дозволяється стоячі пасажири в міжміському автобусі?",
            explanation="У міжміському автобусі стоячі пасажири не дозволяються."
        )
        questions_dict["d7"] = q
        QuizzesQuestions.objects.create(quiz=quiz_d, question=q)
        
        Answer.objects.create(question=q, text="Так, без обмежень", is_correct=False)
        Answer.objects.create(question=q, text="Так, але не більше 5 осіб", is_correct=False)
        Answer.objects.create(question=q, text="Так, але тільки на короткі відстані", is_correct=False)
        Answer.objects.create(question=q, text="Ні, не дозволяються", is_correct=True)
        
        # Вопрос 8
        q = Question.objects.create(
            text="Яка максимальна швидкість руху автобусів на автомагістралях?",
            explanation="На автомагістралях максимальна швидкість руху автобусів становить 90 км/год."
        )
        questions_dict["d8"] = q
        QuizzesQuestions.objects.create(quiz=quiz_d, question=q)
        
        Answer.objects.create(question=q, text="70 км/год", is_correct=False)
        Answer.objects.create(question=q, text="80 км/год", is_correct=False)
        Answer.objects.create(question=q, text="90 км/год", is_correct=True)
        Answer.objects.create(question=q, text="110 км/год", is_correct=False)
        
        # Вопрос 9
        q = Question.objects.create(
            text="Скільки годин на добу водій автобуса може керувати транспортним засобом?",
            explanation="Водій автобуса може керувати транспортним засобом не більше 9 годин на добу."
        )
        questions_dict["d9"] = q
        QuizzesQuestions.objects.create(quiz=quiz_d, question=q)
        
        Answer.objects.create(question=q, text="7 годин", is_correct=False)
        Answer.objects.create(question=q, text="8 годин", is_correct=False)
        Answer.objects.create(question=q, text="9 годин", is_correct=True)
        Answer.objects.create(question=q, text="10 годин", is_correct=False)
        
        # Вопрос 10
        q = Question.objects.create(
            text="Хто відповідає за безпеку пасажирів під час перевезення?",
            explanation="За безпеку пасажирів під час перевезення відповідає водій автобуса."
        )
        questions_dict["d10"] = q
        QuizzesQuestions.objects.create(quiz=quiz_d, question=q)
        
        Answer.objects.create(question=q, text="Водій", is_correct=True)
        Answer.objects.create(question=q, text="Перевізник", is_correct=False)
        Answer.objects.create(question=q, text="Пасажири", is_correct=False)
        Answer.objects.create(question=q, text="Контролер", is_correct=False)
        
        # Вопрос 11
        q = Question.objects.create(
            text="За яких умов дозволяється рух автобуса заднім ходом?",
            explanation="Рух автобуса заднім ходом дозволяється тільки при маневруванні і лише за умови, що це не створить небезпеки для інших учасників руху."
        )
        questions_dict["d11"] = q
        QuizzesQuestions.objects.create(quiz=quiz_d, question=q)
        
        Answer.objects.create(question=q, text="Не дозволяється ніколи", is_correct=False)
        Answer.objects.create(question=q, text="Тільки при маневруванні", is_correct=True)
        Answer.objects.create(question=q, text="Тільки в присутності регулювальника", is_correct=False)
        Answer.objects.create(question=q, text="В будь-якому випадку", is_correct=False)
        
        # Вопрос 12
        q = Question.objects.create(
            text="Чи має право водій автобуса відмовити в перевезенні пасажиру в стані алкогольного сп'яніння?",
            explanation="Водій автобуса має право відмовити в перевезенні пасажиру в стані алкогольного сп'яніння, який може забруднити інших пасажирів або автобус."
        )
        questions_dict["d12"] = q
        QuizzesQuestions.objects.create(quiz=quiz_d, question=q)
        
        Answer.objects.create(question=q, text="Так, має право", is_correct=True)
        Answer.objects.create(question=q, text="Ні, не має права", is_correct=False)
        Answer.objects.create(question=q, text="Тільки за згодою інших пасажирів", is_correct=False)
        Answer.objects.create(question=q, text="Тільки якщо є інший транспорт", is_correct=False)
        
        # Вопрос 13
        q = Question.objects.create(
            text="Як повинен діяти водій автобуса у випадку виникнення несправності під час руху з пасажирами?",
            explanation="У випадку виникнення несправності водій повинен зупинитися в безпечному місці, вжити заходів для висадки пасажирів або їх пересадки в інший транспортний засіб."
        )
        questions_dict["d13"] = q
        QuizzesQuestions.objects.create(quiz=quiz_d, question=q)
        
        Answer.objects.create(question=q, text="Продовжити рух до найближчої станції", is_correct=False)
        Answer.objects.create(question=q, text="Зупинитися для ремонту без висадки пасажирів", is_correct=False)
        Answer.objects.create(question=q, text="Зупинитися в безпечному місці та висадити пасажирів", is_correct=True)
        Answer.objects.create(question=q, text="Зупинитися та викликати поліцію", is_correct=False)
        
        # Вопрос 14
        q = Question.objects.create(
            text="Яким транспортним засобам водій автобуса повинен надати перевагу при відправленні від зупинки?",
            explanation="При відправленні від зупинки водій автобуса повинен надати перевагу транспортним засобам, що рухаються по проїзній частині."
        )
        questions_dict["d14"] = q
        QuizzesQuestions.objects.create(quiz=quiz_d, question=q)
        
        Answer.objects.create(question=q, text="Всім транспортним засобам", is_correct=True)
        Answer.objects.create(question=q, text="Тільки легковим автомобілям", is_correct=False)
        Answer.objects.create(question=q, text="Тільки вантажним автомобілям", is_correct=False)
        Answer.objects.create(question=q, text="Жодним транспортним засобам", is_correct=False)
        
        # Вопрос 15
        q = Question.objects.create(
            text="Де повинен зупинятися автобус для посадки/висадки пасажирів?",
            explanation="Автобус повинен зупинятися для посадки/висадки пасажирів тільки на відповідно позначених зупинках."
        )
        questions_dict["d15"] = q
        QuizzesQuestions.objects.create(quiz=quiz_d, question=q)
        
        Answer.objects.create(question=q, text="У будь-якому місці на вимогу пасажира", is_correct=False)
        Answer.objects.create(question=q, text="Тільки на позначених зупинках", is_correct=True)
        Answer.objects.create(question=q, text="У будь-якому безпечному місці", is_correct=False)
        Answer.objects.create(question=q, text="На перехрестях", is_correct=False)
        
        # Вопрос 16
        q = Question.objects.create(
            text="Чи має право водій автобуса відкривати двері до повної зупинки транспортного засобу?",
            explanation="Водій автобуса не має права відкривати двері до повної зупинки транспортного засобу."
        )
        questions_dict["d16"] = q
        QuizzesQuestions.objects.create(quiz=quiz_d, question=q)
        
        Answer.objects.create(question=q, text="Так, має право", is_correct=False)
        Answer.objects.create(question=q, text="Ні, не має права", is_correct=True)
        Answer.objects.create(question=q, text="Тільки при швидкості до 5 км/год", is_correct=False)
        Answer.objects.create(question=q, text="Тільки на зупинках", is_correct=False)
        
        # Вопрос 17
        q = Question.objects.create(
            text="Які документи повинен мати водій автобуса для здійснення регулярних пасажирських перевезень?",
            explanation="Водій автобуса для здійснення регулярних пасажирських перевезень повинен мати посвідчення водія, реєстраційні документи на автобус, ліцензійну картку, дорожній лист та схему маршруту."
        )
        questions_dict["d17"] = q
        QuizzesQuestions.objects.create(quiz=quiz_d, question=q)
        
        Answer.objects.create(question=q, text="Тільки посвідчення водія", is_correct=False)
        Answer.objects.create(question=q, text="Посвідчення водія та реєстраційні документи", is_correct=False)
        Answer.objects.create(question=q, text="Посвідчення водія, реєстраційні документи та дорожній лист", is_correct=False)
        Answer.objects.create(question=q, text="Посвідчення водія, реєстраційні документи, ліцензійну картку, дорожній лист та схему маршруту", is_correct=True)
        
        # Вопрос 18
        q = Question.objects.create(
            text="Хто має право проводити технічний огляд автобуса перед виїздом на маршрут?",
            explanation="Технічний огляд автобуса перед виїздом на маршрут має право проводити механік з безпеки руху."
        )
        questions_dict["d18"] = q
        QuizzesQuestions.objects.create(quiz=quiz_d, question=q)
        
        Answer.objects.create(question=q, text="Тільки водій", is_correct=False)
        Answer.objects.create(question=q, text="Механік з безпеки руху", is_correct=True)
        Answer.objects.create(question=q, text="Будь-який співробітник автопарку", is_correct=False)
        Answer.objects.create(question=q, text="Поліцейський", is_correct=False)
        
        # Вопрос 19
        q = Question.objects.create(
            text="Яка максимальна кількість стоячих пасажирів дозволена в міському автобусі?",
            explanation="Максимальна кількість стоячих пасажирів у міському автобусі визначається технічними характеристиками транспортного засобу."
        )
        questions_dict["d19"] = q
        QuizzesQuestions.objects.create(quiz=quiz_d, question=q)
        
        Answer.objects.create(question=q, text="5 осіб на 1 кв. метр", is_correct=False)
        Answer.objects.create(question=q, text="Згідно з технічними характеристиками автобуса", is_correct=True)
        Answer.objects.create(question=q, text="Не більше кількості сидячих місць", is_correct=False)
        Answer.objects.create(question=q, text="Без обмежень", is_correct=False)
        
        # Вопрос 20
        q = Question.objects.create(
            text="Чи може автобус рухатися по крайній лівій смузі на дорозі, що має три і більше смуг для руху в одному напрямку?",
            explanation="Автобусу заборонено рухатися по крайній лівій смузі на дорозі, що має три і більше смуг для руху в одному напрямку, за винятком виконання лівого повороту або розвороту."
        )
        questions_dict["d20"] = q
        QuizzesQuestions.objects.create(quiz=quiz_d, question=q)
        
        Answer.objects.create(question=q, text="Так, без обмежень", is_correct=False)
        Answer.objects.create(question=q, text="Ні, це заборонено", is_correct=False)
        Answer.objects.create(question=q, text="Тільки для виконання лівого повороту або розвороту", is_correct=True)
        Answer.objects.create(question=q, text="Тільки для обгону", is_correct=False)
        
        # Вопрос 21
        q = Question.objects.create(
            text="Чи повинен водій автобуса оголошувати назви зупинок?",
            explanation="Водій автобуса або інша уповноважена особа (кондуктор) повинні оголошувати назви зупинок."
        )
        questions_dict["d21"] = q
        QuizzesQuestions.objects.create(quiz=quiz_d, question=q)
        
        Answer.objects.create(question=q, text="Так, повинен", is_correct=True)
        Answer.objects.create(question=q, text="Ні, не повинен", is_correct=False)
        Answer.objects.create(question=q, text="Тільки кінцеві зупинки", is_correct=False)
        Answer.objects.create(question=q, text="Тільки на прохання пасажирів", is_correct=False)
        
        # Вопрос 22
        q = Question.objects.create(
            text="Коли водій автобуса повинен проходити щозмінний медичний огляд?",
            explanation="Водій автобуса повинен проходити щозмінний медичний огляд перед виїздом на маршрут."
        )
        questions_dict["d22"] = q
        QuizzesQuestions.objects.create(quiz=quiz_d, question=q)
        
        Answer.objects.create(question=q, text="Перед виїздом на маршрут", is_correct=True)
        Answer.objects.create(question=q, text="Після закінчення зміни", is_correct=False)
        Answer.objects.create(question=q, text="Раз на тиждень", is_correct=False)
        Answer.objects.create(question=q, text="На вимогу адміністрації", is_correct=False)
        
        print(f"Created {len(questions_dict)} questions for Category D")
        return True
    except Exception as e:
        print(f"Error in create_category_d_data: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Running category_d_questions.py script")
    success = create_category_d_data()
    sys.exit(0 if success else 1)
