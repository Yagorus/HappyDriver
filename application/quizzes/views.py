from datetime import date, datetime
from django.shortcuts import render, get_object_or_404, redirect
from accounts.utils import custom_login_required
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser
from .models import Quiz, Question, Answer, UsersQuizzes, Result, QuizzesQuestions
from .forms import CategoryForm
from accounts.models import Subscription
from django.http import JsonResponse
from .liqpay3 import LiqPay
from dotenv import load_dotenv
import os
from django.contrib import messages
import random
from django.utils import timezone


load_dotenv()

your_public_key = os.getenv('your_public_key')
your_private_key = os.getenv('your_private_key')


def home_page(request):
    # Debug information
    print("=== HOME PAGE VIEW CALLED ===")
    try:
        from quizzes.models import Quiz
        latest_quiz = Quiz.objects.order_by('-created_at').first()
        print(f"Latest quiz: {latest_quiz}")
        all_quizzes = Quiz.objects.all()
        print(f"All quizzes count: {all_quizzes.count()}")
        for quiz in all_quizzes:
            print(f"  - {quiz.id}: {quiz.title}")
    except Exception as e:
        print(f"Error in debug code: {e}")
    # Debug information
    print("=== HOME PAGE VIEW CALLED ===")
    latest_quiz = Quiz.objects.order_by('-created_at').first()
    print(f"Latest quiz: {latest_quiz}")
    all_quizzes = Quiz.objects.all()
    print(f"All quizzes count: {all_quizzes.count()}")
    for quiz in all_quizzes:
        print(f"  - {quiz.id}: {quiz.title}")
    users_= CustomUser.objects.filter(is_staff=False).count()
    questions = Question.objects.all().count()
    quizzes = Quiz.objects.filter(is_random=False).order_by('-created_at')
    latest_quiz = quizzes[0] if quizzes else None
    context = {
            'users_count': users_,
            'questions_count': questions,
            'quizzes': quizzes,
            'latest_quiz': latest_quiz.title if latest_quiz else "No quizzes available" if latest_quiz else "No quizzes available" if latest_quiz else "No quizzes available" if latest_quiz else "No quizzes available" if latest_quiz else "No quizzes available" if latest_quiz else "No quizzes available" if latest_quiz else "No quizzes available" if latest_quiz else "No quizzes available" if latest_quiz else "No quizzes available" if latest_quiz else "No quizzes available" if latest_quiz else "No quizzes available" if latest_quiz else "No quizzes available" if latest_quiz else "No quizzes available" if latest_quiz else "No quizzes available" if latest_quiz else "No quizzes available" if latest_quiz else "No quizzes available" if latest_quiz else "No quizzes available" if latest_quiz else "No quizzes available" if latest_quiz else "No quizzes available" if latest_quiz else "No quizzes available" if latest_quiz else "No quizzes available" if latest_quiz else "No quizzes available" if latest_quiz else "No quizzes available" if latest_quiz else "No quizzes available" if latest_quiz else "No quizzes available" if latest_quiz else "No quizzes available" if latest_quiz else "No quizzes available" if latest_quiz else "No quizzes available" if latest_quiz else "No quizzes available" if latest_quiz else "No quizzes available" if latest_quiz else "No quizzes available" if latest_quiz else "No quizzes available" if latest_quiz else "No quizzes available" if latest_quiz else "No quizzes available" if latest_quiz else "No quizzes available",
        }
    return render(request, "home.html", context)


@custom_login_required
def get_topic_quizzes(request):
    quizzes = Quiz.objects.filter(category="ALL", is_random=False)
    return render(request, "quizzes/quizzes.html", {'quizzes': quizzes, 'title': 'Тести ПДР по темам'})


@custom_login_required
def get_category_quizzes(request, category):
    quizzes = Quiz.objects.filter(is_random=False, category__in=["ALL", category]).order_by('-created_at')
    return render(request, "quizzes/quizzes.html", {'quizzes': quizzes, 'title': 'Тести ПДР по категоріях прав'})


@custom_login_required
def get_paper_quizzes(request):
    subscriptions = Subscription.objects.filter(user=request.user).order_by("-finished_at")
    if not subscriptions or subscriptions[0].finished_at < date.today():
        return redirect('pay')

    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.cleaned_data['category']
            random_number = random.randint(100000, 999999)
            quiz = Quiz.objects.create(title=f"Білет #{random_number}", category=category, is_random=True)
            quizzes = Quiz.objects.filter(category__in=[category])
            questions = Question.objects.filter(quiz_questions__quiz__in=quizzes)
            count = 20 if questions.count() > 20 else questions.count()
            random_questions = questions.order_by('?')[:count] 
            for question in random_questions:
                QuizzesQuestions.objects.create(quiz=quiz, question=question)
            return redirect("get_quiz", quiz.pk)
    else:
        form = CategoryForm()

    return render(request, "quizzes/get_paper_quiz.html", {
        'title': 'Випадковий білет',
        'form': form
    })


@custom_login_required
def add_subscription(request):
    subscriptions = Subscription.objects.filter(user=request.user).order_by("-finished_at")
    if not subscriptions or subscriptions[0].finished_at < date.today():
        subscription = Subscription(user=request.user)
        subscription.save()
    return JsonResponse({'success': True})


@custom_login_required
def get_quizzes(request):
    return render(request, "quizzes/choose_quiz_type.html", {'title': 'Тести ПДР'})


@custom_login_required
def choose_quiz_category(request):
    return render(request, "quizzes/choose_quiz_category.html", {'title': 'Тести ПДР за категоріями'})


@custom_login_required
def get_quiz(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    print(quiz)
    user_quiz = UsersQuizzes.objects.create(user=request.user, quiz=quiz)
    user_quiz.save()
    return render(request, "quizzes/get_quiz.html", {'quiz': quiz, 'title': f'Тест ПДР: {quiz.title}'})


@custom_login_required
def submit_quiz_results(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    user_quiz = UsersQuizzes.objects.filter(user=request.user, quiz=quiz, finished_at__isnull=True).last()

    if request.method == 'POST':
        user_answers = request.POST.getlist('answers[]')
        for answer_id in user_answers:
            answer = get_object_or_404(Answer, id=answer_id)
            Result.objects.create(
                user_quiz=user_quiz,
                answer=answer
            )
        user_quiz.finished_at = timezone.now()
        user_quiz.save()
        return JsonResponse({'message': 'Результати успішно відправлені!'})


@login_required
def get_history_quizzes_results(request, pk, filter):
    user = get_object_or_404(CustomUser, pk=pk)
    if filter == "all":
        user_quizzes = UsersQuizzes.objects.filter(user=user, finished_at__isnull=False).order_by("-finished_at")

    elif filter == "by-topics":
        user_quizzes = UsersQuizzes.objects.filter(
            user=user,
            quiz__category="ALL",
            quiz__is_random=False,
            finished_at__isnull=False
        ).order_by("-finished_at")

    elif filter == "by-paper":
        user_quizzes = UsersQuizzes.objects.filter(
            user=user, 
            quiz__is_random=True, 
            finished_at__isnull=False
        ).order_by("-finished_at")

    elif "by-category-" in filter:
        category = filter.split("-")[-1].upper()
        user_quizzes = UsersQuizzes.objects.filter(
            user=user, 
            quiz__category=category, 
            quiz__is_random=False, 
            finished_at__isnull=False
        ).order_by("-finished_at")
    
    count = user_quizzes.count()
    print(count)
    return render(request, "quizzes/history_data.html", {
        'user_quizzes': user_quizzes, 
        'count': count, 
        'title': 'Історія проходжень',
        'user_pk': pk
    })


@custom_login_required
def pay(request):
    subscriptions = Subscription.objects.filter(user=request.user).order_by("-finished_at")
    if not subscriptions or subscriptions[0].finished_at < date.today():
        return render(request, "quizzes/payment.html")

    messages.success(request, "Ви вже активували підписку.")
    return redirect('home')


def set_message(request):
    if request.method == 'POST':
        message = request.POST.get('message', '')
        if message:
            messages.error(request, message)
        return JsonResponse({'status': 'success'})
