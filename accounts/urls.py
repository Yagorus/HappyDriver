from django.urls import path
from .views import *


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout'),
    path('edit-account/', edit_user, name='edit_user'),
    path('delete-account/<int:pk>/', delete_user, name='delete_user'),

    path('questions/', QuestionList.as_view(), name='question_list'),
    path('create-quiz/', create_quiz, name='create_quiz'),
    path('create-question/', add_question, name='create_question'),
    path('delete-question/<int:question_id>/', delete_question, name='delete_question'),

    path('users/', ListUsers.as_view(), name='user_list'),
    path('add-assistant/', add_assistant, name='add_assistant'),
]
