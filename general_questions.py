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

def create_general_questions_data():
    try:
        print("Creating questions for General Traffic Rules (Загальні правила дорожнього руху)...")
        
        # Находим квиз для общих правил
        quiz_common = Quiz.objects.filter(category="ALL").first()
        
        if quiz_common:
            print(f"Found existing quiz Common: {quiz_common.title}")
            # Очищаем существующие вопросы для этого квиза
            print(f"Clearing all existing questions for Common quiz")
            QuizzesQuestions.objects.filter(quiz=quiz_common).delete()
        else:
            # Создаем новый квиз
            quiz_common = Quiz.objects.create(
                title="Загальні правила дорожнього руху",
                category="ALL",
                is_random=False
            )
            print(f"Created new quiz Common: {quiz_common.title}")
        
        # Создаем словарь для хранения созданных вопросов
        questions_dict = {}
        
        # Вопрос 1
        q = Question.objects.create(
            text="Що означає жовтий сигнал світлофора?",
            explanation="Жовтий сигнал світлофора забороняє рух і попереджає про наступну зміну сигналів."
        )
        questions_dict["common1"] = q
        QuizzesQuestions.objects.create(quiz=quiz_common, question=q)
        
        Answer.objects.create(question=q, text="Дозволяє рух", is_correct=False)
        Answer.objects.create(question=q, text="Забороняє рух і попереджає про наступну зміну сигналів", is_correct=True)
        Answer.objects.create(question=q, text="Дозволяє рух, але тільки прямо", is_correct=False)
        Answer.objects.create(question=q, text="Дозволяє тільки підготуватися до руху", is_correct=False)
        
        # Вопрос 2
        q = Question.objects.create(
            text="Що означає дорожній знак 'STOP'?",
            explanation="Знак 'STOP' (2.2) вимагає обов'язкової зупинки перед перехрестям. Продовжувати рух можна тільки переконавшись, що це не створить перешкод іншим транспортним засобам."
        )
        questions_dict["common2"] = q
        QuizzesQuestions.objects.create(quiz=quiz_common, question=q)
        
        Answer.objects.create(question=q, text="Стоп на вимогу поліції", is_correct=False)
        Answer.objects.create(question=q, text="Обов'язкова зупинка перед перехрестям", is_correct=True)
        Answer.objects.create(question=q, text="Заборона в'їзду", is_correct=False)
        Answer.objects.create(question=q, text="Стоянка заборонена", is_correct=False)
        
        # Вопрос 3
        q = Question.objects.create(
            text="На якій відстані від пішохідного переходу заборонено зупинку транспортних засобів?",
            explanation="Зупинка заборонена ближче 10 метрів від пішохідного переходу."
        )
        questions_dict["common3"] = q
        QuizzesQuestions.objects.create(quiz=quiz_common, question=q)
        
        Answer.objects.create(question=q, text="5 метрів", is_correct=False)
        Answer.objects.create(question=q, text="10 метрів", is_correct=True)
        Answer.objects.create(question=q, text="15 метрів", is_correct=False)
        Answer.objects.create(question=q, text="20 метрів", is_correct=False)
        
        # Вопрос 4
        q = Question.objects.create(
            text="Яке правило діє на нерегульованому перехресті рівнозначних доріг?",
            explanation="На нерегульованому перехресті рівнозначних доріг водій повинен дати дорогу транспортному засобу, що наближається справа."
        )
        questions_dict["common4"] = q
        QuizzesQuestions.objects.create(quiz=quiz_common, question=q)
        
        Answer.objects.create(question=q, text="Перевага у того, хто рухається прямо", is_correct=False)
        Answer.objects.create(question=q, text="Перевага у того, хто рухається з більшою швидкістю", is_correct=False)
        Answer.objects.create(question=q, text="Перевага у того, хто наближається зліва", is_correct=False)
        Answer.objects.create(question=q, text="Перевага у того, хто наближається справа", is_correct=True)
        
        # Вопрос 5
        q = Question.objects.create(
            text="Яка максимальна допустима концентрація алкоголю в крові водія?",
            explanation="Максимальна допустима концентрація алкоголю в крові водія становить 0,2 проміле."
        )
        questions_dict["common5"] = q
        QuizzesQuestions.objects.create(quiz=quiz_common, question=q)
        
        Answer.objects.create(question=q, text="0,0 проміле", is_correct=False)
        Answer.objects.create(question=q, text="0,2 проміле", is_correct=True)
        Answer.objects.create(question=q, text="0,5 проміле", is_correct=False)
        Answer.objects.create(question=q, text="0,8 проміле", is_correct=False)
        
        # Вопрос 6
        q = Question.objects.create(
            text="Що означає термін 'дорожньо-транспортна пригода'?",
            explanation="Дорожньо-транспортна пригода — подія, що сталася під час руху транспортного засобу, внаслідок якої загинули або поранені люди чи завдані матеріальні збитки."
        )
        questions_dict["common6"] = q
        QuizzesQuestions.objects.create(quiz=quiz_common, question=q)
        
        Answer.objects.create(question=q, text="Будь-яке порушення Правил дорожнього руху", is_correct=False)
        Answer.objects.create(question=q, text="Подія, що сталася під час руху транспортного засобу, внаслідок якої загинули або поранені люди чи завдані матеріальні збитки", is_correct=True)
        Answer.objects.create(question=q, text="Зіткнення двох або більше транспортних засобів", is_correct=False)
        Answer.objects.create(question=q, text="Наїзд на пішохода", is_correct=False)
        
        # Вопрос 7
        q = Question.objects.create(
            text="Яка відстань вважається недостатньою видимістю?",
            explanation="Недостатня видимість - видимість дороги в напрямку руху менше 300 м у сутінках, в умовах туману, дощу, снігопаду тощо."
        )
        questions_dict["common7"] = q
        QuizzesQuestions.objects.create(quiz=quiz_common, question=q)
        
        Answer.objects.create(question=q, text="Менше 100 м", is_correct=False)
        Answer.objects.create(question=q, text="Менше 200 м", is_correct=False)
        Answer.objects.create(question=q, text="Менше 300 м", is_correct=True)
        Answer.objects.create(question=q, text="Менше 500 м", is_correct=False)
        
        # Вопрос 8
        q = Question.objects.create(
            text="Які світлові прилади повинні бути увімкнені на транспортному засобі у світлу пору доби?",
            explanation="У світлу пору доби на транспортному засобі повинні бути увімкнені денні ходові вогні або ближнє світло фар."
        )
        questions_dict["common8"] = q
        QuizzesQuestions.objects.create(quiz=quiz_common, question=q)
        
        Answer.objects.create(question=q, text="Габаритні вогні", is_correct=False)
        Answer.objects.create(question=q, text="Денні ходові вогні або ближнє світло фар", is_correct=True)
        Answer.objects.create(question=q, text="Дальнє світло фар", is_correct=False)
        Answer.objects.create(question=q, text="Протитуманні фари", is_correct=False)
        
        # Вопрос 9
        q = Question.objects.create(
            text="Хто має перевагу на регульованому перехресті при зеленому сигналі світлофора?",
            explanation="При зеленому сигналі світлофора водій, що повертає, повинен дати дорогу пішоходам, які переходять проїзну частину, на яку він повертає, та велосипедистам, які рухаються прямо."
        )
        questions_dict["common9"] = q
        QuizzesQuestions.objects.create(quiz=quiz_common, question=q)
        
        Answer.objects.create(question=q, text="Перевагу має водій, який повертає", is_correct=False)
        Answer.objects.create(question=q, text="Перевагу мають пішоходи і велосипедисти", is_correct=True)
        Answer.objects.create(question=q, text="Перевагу має той, хто перший почав рух", is_correct=False)
        Answer.objects.create(question=q, text="Перевагу має той, хто рухається з більшою швидкістю", is_correct=False)
        
        # Вопрос 10
        q = Question.objects.create(
            text="На яку максимальну відстань можуть виступати вантажі за габарити транспортного засобу ззаду?",
            explanation="Вантажі можуть виступати за габарити транспортного засобу ззаду не більш як на 2 метри."
        )
        questions_dict["common10"] = q
        QuizzesQuestions.objects.create(quiz=quiz_common, question=q)
        
        Answer.objects.create(question=q, text="1 метр", is_correct=False)
        Answer.objects.create(question=q, text="2 метри", is_correct=True)
        Answer.objects.create(question=q, text="2,5 метра", is_correct=False)
        Answer.objects.create(question=q, text="3 метри", is_correct=False)
        
        # Вопрос 11
        q = Question.objects.create(
            text="За якої умови водій може почати обгін?",
            explanation="Водій може починати обгін лише переконавшись, що смуга зустрічного руху вільна на достатній для обгону відстані."
        )
        questions_dict["common11"] = q
        QuizzesQuestions.objects.create(quiz=quiz_common, question=q)
        
        Answer.objects.create(question=q, text="За будь-якої умови", is_correct=False)
        Answer.objects.create(question=q, text="Якщо попереду автомобіль рухається повільно", is_correct=False)
        Answer.objects.create(question=q, text="Переконавшись, що смуга зустрічного руху вільна на достатній для обгону відстані", is_correct=True)
        Answer.objects.create(question=q, text="Якщо дорожня розмітка це дозволяє", is_correct=False)
        
        # Вопрос 12
        q = Question.objects.create(
            text="В якому віці можна отримати посвідчення водія категорії B?",
            explanation="Посвідчення водія категорії B можна отримати в 18 років."
        )
        questions_dict["common12"] = q
        QuizzesQuestions.objects.create(quiz=quiz_common, question=q)
        
        Answer.objects.create(question=q, text="16 років", is_correct=False)
        Answer.objects.create(question=q, text="17 років", is_correct=False)
        Answer.objects.create(question=q, text="18 років", is_correct=True)
        Answer.objects.create(question=q, text="21 рік", is_correct=False)
        
        # Вопрос 13
        q = Question.objects.create(
            text="Що таке сліпа зона автомобіля?",
            explanation="Сліпа зона - це область навколо автомобіля, яку водій не може побачити ні через дзеркала, ні безпосередньо."
        )
        questions_dict["common13"] = q
        QuizzesQuestions.objects.create(quiz=quiz_common, question=q)
        
        Answer.objects.create(question=q, text="Зона перед капотом автомобіля", is_correct=False)
        Answer.objects.create(question=q, text="Зона за лобовим склом", is_correct=False)
        Answer.objects.create(question=q, text="Область навколо автомобіля, яку водій не може побачити", is_correct=True)
        Answer.objects.create(question=q, text="Зона поганої видимості на дорозі", is_correct=False)
        
        # Вопрос 14
        q = Question.objects.create(
            text="Як позначається автомобіль, яким керує особа, що навчається водінню?",
            explanation="Автомобіль, яким керує особа, що навчається водінню, повинен бути позначений спереду і ззаду знаком 'У' (учбовий транспортний засіб)."
        )
        questions_dict["common14"] = q
        QuizzesQuestions.objects.create(quiz=quiz_common, question=q)
        
        Answer.objects.create(question=q, text="Знаком 'У' (учбовий транспортний засіб)", is_correct=True)
        Answer.objects.create(question=q, text="Знаком '!' (увага)", is_correct=False)
        Answer.objects.create(question=q, text="Спеціальними прапорцями", is_correct=False)
        Answer.objects.create(question=q, text="Червоними ліхтарями", is_correct=False)
        
        # Вопрос 15
        q = Question.objects.create(
            text="В який час доби необхідно вмикати ближнє світло фар?",
            explanation="Ближнє світло фар необхідно вмикати цілодобово на всіх транспортних засобах, що рухаються дорогами."
        )
        questions_dict["common15"] = q
        QuizzesQuestions.objects.create(quiz=quiz_common, question=q)
        
        Answer.objects.create(question=q, text="Тільки в темну пору доби", is_correct=False)
        Answer.objects.create(question=q, text="Тільки в умовах недостатньої видимості", is_correct=False)
        Answer.objects.create(question=q, text="Цілодобово", is_correct=True)
        Answer.objects.create(question=q, text="Тільки під час дощу або снігопаду", is_correct=False)
        
        # Вопрос 16
        q = Question.objects.create(
            text="Хто має перевагу при виїзді з прилеглої території?",
            explanation="При виїзді з прилеглої території водій повинен дати дорогу транспортним засобам, що рухаються по дорозі, та пішоходам, що рухаються тротуаром."
        )
        questions_dict["common16"] = q
        QuizzesQuestions.objects.create(quiz=quiz_common, question=q)
        
        Answer.objects.create(question=q, text="Водій, що виїжджає з прилеглої території", is_correct=False)
        Answer.objects.create(question=q, text="Пішоходи та транспортні засоби, що рухаються по дорозі", is_correct=True)
        Answer.objects.create(question=q, text="Перевагу надають за знаками пріоритету", is_correct=False)
        Answer.objects.create(question=q, text="Перевагу має той, хто перший почав рух", is_correct=False)
        
        # Вопрос 17
        q = Question.objects.create(
            text="Як правильно обрати інтервал між транспортними засобами під час руху?",
            explanation="Інтервал між транспортними засобами під час руху має бути безпечним і залежить від швидкості, дорожніх та погодних умов, а також стану транспортного засобу."
        )
        questions_dict["common17"] = q
        QuizzesQuestions.objects.create(quiz=quiz_common, question=q)
        
        Answer.objects.create(question=q, text="Завжди не менше 1 метра", is_correct=False)
        Answer.objects.create(question=q, text="Залежно від швидкості, дорожніх та погодних умов", is_correct=True)
        Answer.objects.create(question=q, text="Завжди не менше 2 метрів", is_correct=False)
        Answer.objects.create(question=q, text="Завжди не менше половини швидкості в метрах", is_correct=False)
        
        # Вопрос 18
        q = Question.objects.create(
            text="Що означає поняття 'дорожня обстановка, що змінилася'?",
            explanation="Дорожня обстановка, що змінилася - це зміна дорожньої ситуації, яка загрожує безпеці дорожнього руху і вимагає від водія негайних дій для запобігання ДТП."
        )
        questions_dict["common18"] = q
        QuizzesQuestions.objects.create(quiz=quiz_common, question=q)
        
        Answer.objects.create(question=q, text="Зміна погодних умов", is_correct=False)
        Answer.objects.create(question=q, text="Зміна дорожнього покриття", is_correct=False)
        Answer.objects.create(question=q, text="Зміна маршруту руху", is_correct=False)
        Answer.objects.create(question=q, text="Зміна дорожньої ситуації, яка загрожує безпеці руху", is_correct=True)
        
        # Вопрос 19
        q = Question.objects.create(
            text="Чи має право водій користуватися телефоном під час руху?",
            explanation="Водій має право користуватися телефоном під час руху тільки за допомогою технічних засобів, які дозволяють розмовляти без допомоги рук (гарнітура, гучний зв'язок)."
        )
        questions_dict["common19"] = q
        QuizzesQuestions.objects.create(quiz=quiz_common, question=q)
        
        Answer.objects.create(question=q, text="Ні, це категорично заборонено", is_correct=False)
        Answer.objects.create(question=q, text="Так, без обмежень", is_correct=False)
        Answer.objects.create(question=q, text="Так, але тільки при швидкості менше 40 км/год", is_correct=False)
        Answer.objects.create(question=q, text="Так, але тільки за допомогою гарнітури або гучного зв'язку", is_correct=True)
        
        # Вопрос 20
        q = Question.objects.create(
            text="Яка максимальна дозволена швидкість руху на житлових територіях та пішохідних зонах?",
            explanation="На житлових територіях та пішохідних зонах максимальна дозволена швидкість руху становить 20 км/год."
        )
        questions_dict["common20"] = q
        QuizzesQuestions.objects.create(quiz=quiz_common, question=q)
        
        Answer.objects.create(question=q, text="10 км/год", is_correct=False)
        Answer.objects.create(question=q, text="20 км/год", is_correct=True)
        Answer.objects.create(question=q, text="30 км/год", is_correct=False)
        Answer.objects.create(question=q, text="40 км/год", is_correct=False)
        
        # Вопрос 21
        q = Question.objects.create(
            text="Що означають зелені стрілки на додатковій секції світлофора?",
            explanation="Зелені стрілки на додатковій секції світлофора дозволяють рух у вказаному напрямку при увімкненому червоному чи жовтому сигналі світлофора."
        )
        questions_dict["common21"] = q
        QuizzesQuestions.objects.create(quiz=quiz_common, question=q)
        
        Answer.objects.create(question=q, text="Забороняють рух у вказаному напрямку", is_correct=False)
        Answer.objects.create(question=q, text="Дозволяють рух у вказаному напрямку при увімкненому червоному чи жовтому сигналі", is_correct=True)
        Answer.objects.create(question=q, text="Попереджають про зміну сигналу", is_correct=False)
        Answer.objects.create(question=q, text="Дозволяють рух тільки громадському транспорту", is_correct=False)
        
        # Вопрос 22
        q = Question.objects.create(
            text="Які документи повинен мати при собі водій механічного транспортного засобу?",
            explanation="Водій механічного транспортного засобу повинен мати при собі посвідчення водія, свідоцтво про реєстрацію транспортного засобу, поліс обов'язкового страхування."
        )
        questions_dict["common22"] = q
        QuizzesQuestions.objects.create(quiz=quiz_common, question=q)
        
        Answer.objects.create(question=q, text="Тільки посвідчення водія", is_correct=False)
        Answer.objects.create(question=q, text="Посвідчення водія та свідоцтво про реєстрацію", is_correct=False)
        Answer.objects.create(question=q, text="Посвідчення водія, свідоцтво про реєстрацію та страховий поліс", is_correct=True)
        Answer.objects.create(question=q, text="Паспорт громадянина", is_correct=False)
        
        # Вопрос 23
        q = Question.objects.create(
            text="Як повинен діяти водій у разі засліплення світлом фар зустрічного автомобіля?",
            explanation="У разі засліплення водій повинен увімкнути аварійну сигналізацію і, не змінюючи смуги руху, знизити швидкість і зупинитися."
        )
        questions_dict["common23"] = q
        QuizzesQuestions.objects.create(quiz=quiz_common, question=q)
        
        Answer.objects.create(question=q, text="Засигналити зустрічному автомобілю", is_correct=False)
        Answer.objects.create(question=q, text="Увімкнути дальнє світло фар", is_correct=False)
        Answer.objects.create(question=q, text="Увімкнути аварійну сигналізацію, знизити швидкість і зупинитися", is_correct=True)
        Answer.objects.create(question=q, text="Різко загальмувати", is_correct=False)
        
        # Вопрос 24
        q = Question.objects.create(
            text="Що означає синя розмітка на проїзній частині?",
            explanation="Синя розмітка позначає платну парковку або місця для паркування спеціальних транспортних засобів."
        )
        questions_dict["common24"] = q
        QuizzesQuestions.objects.create(quiz=quiz_common, question=q)
        
        Answer.objects.create(question=q, text="Місця для парковки людей з інвалідністю", is_correct=False)
        Answer.objects.create(question=q, text="Місця для паркування спеціальних транспортних засобів", is_correct=True)
        Answer.objects.create(question=q, text="Напрямок руху", is_correct=False)
        Answer.objects.create(question=q, text="Зону для розвороту", is_correct=False)
        
        # Вопрос 25
        q = Question.objects.create(
            text="Які дії водія у випадку ДТП?",
            explanation="У випадку ДТП водій зобов'язаний негайно зупинитися, увімкнути аварійну сигналізацію, встановити знак аварійної зупинки, не переміщати предмети, що мають відношення до пригоди, вжити заходів для надання першої медичної допомоги, викликати поліцію та швидку допомогу."
        )
        questions_dict["common25"] = q
        QuizzesQuestions.objects.create(quiz=quiz_common, question=q)
        
        Answer.objects.create(question=q, text="Продовжити рух і повідомити про ДТП пізніше", is_correct=False)
        Answer.objects.create(question=q, text="Залишити місце ДТП, якщо немає постраждалих", is_correct=False)
        Answer.objects.create(question=q, text="Зупинитися, увімкнути аварійну сигналізацію, встановити знак аварійної зупинки, надати першу допомогу, викликати поліцію", is_correct=True)
        Answer.objects.create(question=q, text="Перемістити автомобілі з проїзної частини", is_correct=False)
        
        print(f"Created {len(questions_dict)} questions for Common Traffic Rules")
        return True
    except Exception as e:
        print(f"Error in create_general_questions_data: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Running general_questions.py script")
    success = create_general_questions_data()
    sys.exit(0 if success else 1)
