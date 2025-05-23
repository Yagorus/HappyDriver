from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate


class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повторіть пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = ('firstname', 'lastname', 'email', 'age')
        widgets = {
            'firstname': forms.TextInput(attrs={'class': 'form-control'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'step': '1'})
        }


class UserLoginForm(forms.ModelForm):

    class Meta:
        fields = ['email', 'password']
        model = CustomUser
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control custom-email-class'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control custom-password-class'
            })
        }

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        if email is not None and password:
            self.user_cache = authenticate(email=email, password=password)
            if self.user_cache is None:
                raise forms.ValidationError("Пошта або пароль некоректні.")
        return self.cleaned_data

    def get_user(self):
        return self.user_cache


class UserEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'firstname', 'lastname', 'age')
        widgets = {
            'firstname': forms.TextInput(attrs={'class': 'form-control'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'step': '1'}),
        }
