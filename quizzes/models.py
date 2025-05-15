from django.db import models
from accounts.models import CustomUser


CATEGORY_CHOICES = (
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
    ('E', 'E'),
    ('ALL', 'Усі')
)


class Quiz(models.Model):
    title = models.CharField(max_length=255, unique=True)
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES)
    is_random = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def delete_quiz(self):
        self.quiz_questions.all().delete()
        UsersQuizzes.objects.filter(quiz=self).delete()
        self.delete()


class Question(models.Model):
    text = models.TextField()
    explanation = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='questions_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50] 
    
    def get_correct_answer(self):
        return self.answers.filter(is_correct=True).first()
    
    def delete_question(self):
        self.answers.all().delete()
        self.quiz_questions.all().delete()
        self.delete()


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    text = models.TextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class QuizzesQuestions(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='quiz_questions', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name='quiz_questions', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.quiz.title} - {self.question.text[:50]}'


class UsersQuizzes(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    started_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.firstname} - {self.quiz.title} [started at: {self.started_at}]'


class Result(models.Model):
    user_quiz = models.ForeignKey(UsersQuizzes, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    def __str__(self):
        return f'Result for {self.user_quiz.user.firstname} in {self.user_quiz.quiz.title}'
