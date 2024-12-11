from datetime import datetime
from django.shortcuts import render, get_object_or_404
from accounts.utils import custom_login_required
from .models import Quiz, Question, Answer, UsersQuizzes, Result
from django.http import JsonResponse


@custom_login_required
def get_topic_quizzes(request):
    quizzes = Quiz.objects.filter(category="ALL", is_random=False)
    return render(request, "quizzes/quizzes.html", {'quizzes': quizzes, 'title': 'Тести ПДР по темам'})


@custom_login_required
def get_category_quizzes(request, category):
    quizzes = Quiz.objects.filter(category=category)
    return render(request, "quizzes/quizzes.html", {'quizzes': quizzes, 'title': 'Тести ПДР по категоріях прав'})


@custom_login_required
def get_paper_quizzes(request):
    quizzes = Quiz.objects.filter(is_random=True)
    return render(request, "quizzes/quizzes.html", {'quizzes': quizzes, 'title': 'Тести ПДР по білетах'})


@custom_login_required
def get_quizzes(request):
    return render(request, "quizzes/choose_quiz_type.html", {'title': 'Тести ПДР'})


@custom_login_required
def choose_quiz_category(request):
    return render(request, "quizzes/choose_quiz_category.html", {'title': 'Тести ПДР'})


@custom_login_required
def get_quiz(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    user_quiz = UsersQuizzes.objects.create(user=request.user, quiz=quiz)
    user_quiz.save()
    return render(request, "quizzes/get_quiz.html", {'quiz': quiz})


@custom_login_required
def submit_quiz_results(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    user_quiz = UsersQuizzes.objects.get(user=request.user, quiz=quiz, finished_at__isnull=True)

    if request.method == 'POST':
        user_answers = request.POST.getlist('answers[]')
        for answer_id in user_answers:
            answer = get_object_or_404(Answer, id=answer_id)
            Result.objects.create(
                user_quiz=user_quiz,
                answer=answer
            )
        user_quiz.finished_at = datetime.utcnow()
        user_quiz.save()

        return JsonResponse({'message': 'Результаты успешно отправлены!'})
    return JsonResponse({'error': 'Неверный метод запроса.'}, status=400)


@custom_login_required
def get_history_quizzes_results(request, filter):
    if filter == "all":
        user_quizzes = UsersQuizzes.objects.filter(user=request.user, finished_at__isnull=False).order_by("-finished_at")

    elif filter == "by-topics":
        user_quizzes = UsersQuizzes.objects.filter(
            user=request.user,
            quiz__category="ALL",
            quiz__is_random=False,
            finished_at__isnull=False
        ).order_by("-finished_at")

    elif filter == "by-paper":
        user_quizzes = UsersQuizzes.objects.filter(
            user=request.user, 
            quiz__is_random=True, 
            finished_at__isnull=False
        ).order_by("-finished_at")

    elif "by-category-" in filter:
        category = filter.split("-")[-1].upper()
        user_quizzes = UsersQuizzes.objects.filter(
            user=request.user, 
            quiz__category=category, 
            quiz__is_random=False, 
            finished_at__isnull=False
        ).order_by("-finished_at")
    return render(request, "quizzes/history_data.html", {'user_quizzes': user_quizzes})
