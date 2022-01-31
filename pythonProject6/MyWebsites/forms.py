from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from .models import Task  #подключаем модель с которой будет работать форма
from django.forms import ModelForm , TextInput , Textarea

class TaskForm(ModelForm):
    class Meta: # класс для указания настроек
        model = Task
        fields = ["title","task"] # указываем поля , с которыми будемработать в форме
        widgets = { # создаем словарь для хранения характеристик полей формы
            "title": TextInput(attrs={
                'class':"form-control",
                'placeholder':"Введите название"
            }),
            "task": Textarea(attrs = {
                'class':"form-control",
                'placeholder':"Введите описание"
            })
        }

class AuthUserForm(AuthenticationForm,ModelForm):
    class Meta: # класс для указания настроек
        model = User
        fields = ["username","password"] # указываем поля , с которыми будемработать в форме

class RegisterUserForm(ModelForm):
    class Meta: # класс для указания настроек
        model = User
        fields = ["username","password"] # указываем поля , с которыми будемработать в форме

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

