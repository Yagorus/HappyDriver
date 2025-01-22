import json
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserLoginForm, UserRegisterForm, UserEditForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.views.generic import ListView
from .models import CustomUser
from quizzes.models import Quiz, Question, Answer, UsersQuizzes, Result
from .utils import custom_login_required, staff_login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # registration only
            form.save()
            messages.success(request, 'Успішна реєстрація!')
            return redirect('signin')

            # registration and login
            # user = form.save()
            # login(request, user)
            # messages.success(request, 'Успішна реєстрація! Ви увійшли!')
            # return redirect('home')
        else:
            messages.error(request, form.errors)
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/login.html', {'form': form, 'title': 'Реєстрація'})


def signin(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Ви увійшли')
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form, 'title': 'Вхід'})


def signout(request):
    logout(request)
    return redirect('home')


@method_decorator(staff_login_required, name='dispatch')
class ListUsers(ListView):
    context_object_name = 'users'
    paginate_by = 10
    model = CustomUser
    template_name = 'accounts/user_list.html'


@staff_login_required
def add_assistant(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True
            user.is_superuser = False
            user.save()
            messages.success(request, 'Ви додали помічника!')
            return redirect('user_list')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/signup.html',
                  {'form': form, 'title': 'Додати помічника'})


@login_required
def edit_user(request):
    user = get_object_or_404(CustomUser, pk=request.user.pk)
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваші дані успішно відредаговано!')
            return redirect('home')
    else:
        form = UserEditForm(instance=user)
    return render(request, 'accounts/login.html',
                  {'form': form, 'title': 'Редагування профілю'})


@custom_login_required
def delete_user(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)

    quizzes = UsersQuizzes.objects.filter(user=user)
    for quiz in quizzes:
        results = Result.objects.filter(user_quiz=quiz)
        for result in results:
            result.delete()
        quiz.delete()

    user.delete()
    return redirect('signout')


@staff_login_required
def create_quiz(request):
    if request.method == 'GET':
        return render(request, 'accounts/create_quiz.html')

    elif request.method == 'POST':
        data = json.loads(request.POST['data'])
        files = request.FILES

        quiz = Quiz.objects.create(
            title=data['testName'],
            category=data['category'],
            is_random=data['isRandom']
        )

        for question_index, question_data in enumerate(data['questions']):
            image_key = f'questions[{question_index}][image]'
            image_file = files.get(image_key) if image_key in files else None

            question = Question.objects.create(
                text=question_data['text'],
                explanation=question_data.get('explanation', ''),
                image=image_file
            )
            quiz.quiz_questions.create(question=question)

            for answer_data in question_data['answers']:
                Answer.objects.create(
                    question=question,
                    text=answer_data['text'],
                    is_correct=answer_data['is_correct']
                )

        return JsonResponse({'message': 'Тестування створено!'}, status=201)
