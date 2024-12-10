from django.urls import path
from .views import get_quizzes, get_topic_quizzes, get_category_quizzes, get_paper_quizzes, choose_quiz_category

urlpatterns = [
    path('quizzes/', get_quizzes, name='get_quizzes'),
    path('choose-category/', choose_quiz_category, name='choose_quiz_category'),
    path('paper-quizzes/', get_paper_quizzes, name='get_paper_quizzes'),
    path('category-quizzes/<str:category>/', get_category_quizzes, name='get_category_quizzes'),
    path('topic-quizzes/', get_topic_quizzes, name='get_topic_quizzes'),
]
