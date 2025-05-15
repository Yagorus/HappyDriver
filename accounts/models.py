from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from datetime import date, timedelta


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        # extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username     = None
    email        = models.CharField(max_length=100, unique=True, verbose_name='Електронна пошта')

    firstname    = models.CharField(max_length=50, blank=True, verbose_name="Ім'я")
    lastname     = models.CharField(max_length=50, blank=True, verbose_name='Прізвище')
    password     = models.CharField(max_length=255, verbose_name='Пароль')
    age          = models.IntegerField(null=False, default=16, validators=[MinValueValidator(16)], verbose_name='Вік')

    is_staff     = models.BooleanField(default=False, verbose_name='Персонал')
    is_superuser = models.BooleanField(default=False, verbose_name='Суперкористувач')
    is_active    = models.BooleanField(default=True, verbose_name='Активний')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    class Meta:
        verbose_name = 'користувач(а)'
        verbose_name_plural = 'користувачі'
        ordering = ['-id']

    def __str__(self):
        return self.email

    @staticmethod
    def get_by_id(user_id):
        custom_user = CustomUser.objects.get(id=user_id)
        return custom_user or None

    @staticmethod
    def get_by_email(email):
        custom_user = CustomUser.objects.get(email=email)
        return custom_user or None


class Subscription(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    started_at = models.DateField(blank=True, null=True)
    finished_at = models.DateField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.started_at = date.today()
        self.finished_at = date.today() + timedelta(days=30)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.firstname} - [started at: {self.started_at}]'
