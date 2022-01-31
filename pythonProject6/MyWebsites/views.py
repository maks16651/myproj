import django.contrib
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render , redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Task
from .forms import TaskForm, AuthUserForm, RegisterUserForm  ##импортируем созданные нами формы



def index(request):
    tasks =Task.objects.order_by('id')   # получаем все атрибуты модели таск  и сортируем их ,чтоб ссначала выводились новые
    return render(request,"MyWebsites/index.html",{'title': 'главная страница сайта','tasks':tasks}) # с помощью метода render передаем на страницу Index данные по ключу Title и Tasks, теперь мы можем использовать эти данные на этой странице

def death(request):
    return render(request,"MyWebsites/about.html")

def creating(request):
    error = ''
    if request.method == "POST": #указываем , что если потльзователь отправляет данныеметодом пост , то происходит следующий рагмент кода
        form = TaskForm(request.POST) # создаем обьект на основе класса таскформ , наполненный данными , которые ввел пользователь
        if form.is_valid(): # проверяем на корректность
            form.save()
            return redirect('home') # после сохранения темы , переадресовываемпользователя на главную страницу методом редирект
        else:
            error = " заполнение не корректно " # если не корректно , присваиваем еррор это значение
    form = TaskForm()
    context = {  #создаем словарь , в котором хранятся обьекты созданные на основе класса форм по ключу фор
        "form": form,
        "error": error
    }
    return render(request,"MyWebsites/creating.html",context)

def themes(request):
    tasks =Task.objects.order_by('id')   # получаем все атрибуты модели таск  и сортируем их ,чтоб ссначала выводились новые
    return render(request,"MyWebsites/themes.html",{'title': 'главная страница сайта','tasks':tasks}) # с помощью метода render выводим на экран страницу по указанному адресу в templates

def billy(request):
    return render(request,"MyWebsites/Billy.html")




class Autorisation(LoginView): ## создаем класс для авторизации на основе класса LoginView из Django
    template_name = 'MyWebsites/login.html'
    form_class = AuthUserForm ##создаем форму авторизации на основе формы созданной нами в forms
    success_url = reverse_lazy('login')

class Registration(CreateView):
    model = User
    template_name = 'MyWebsites/registration.html'
    form_class = RegisterUserForm  ##создаем форму авторизации на основе формы созданной нами в forms
    success_url = reverse_lazy('themes')
    success_msg = "Пользователь успешно зарегистрирован"



