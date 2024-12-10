from django.shortcuts import render
from accounts.utils import custom_login_required
from .models import Quiz, Question, Answer, UsersQuizzes, Result


@custom_login_required
def get_topic_quizzes(request):
    quizzes = Quiz.objects.filter(category="ALL", is_random=False)
    print(quizzes)
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
