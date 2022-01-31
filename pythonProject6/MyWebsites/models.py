from django.db import models

# Create your models here.
class Task(models.Model): #
    title = models.CharField('название', max_length=200) # title содержит CharField - блок данных для хранения текста , при
    # определении CharField надо сообщить джанге ,сколько места надо под него в базе данных , тут мы указали 200 слов
    task =  models.TextField('описание') # textfield это тот же charfield , только может хранить намного больше текста ,'описание' - заголовок
    data = models.DateTimeField(auto_now_add=True) #блок данных DateTimeField нужен для хранения даты и вреени
    # , аргумент auto_now_add=True приказывает джанге автоматически присвоить этому атрибуту текущую дату и время ,
    # когда пользователь создает тему

    def __str__(self): # возвращает строковое представление модели
        return self.title # возвращает строку , хранящуюся в атрибуте text

    class Meta: #класс для изменения имени таск на другое
        verbose_name = 'задача' # имя для единичного числа
        verbose_name_plural = 'задачи' # имя для множественного числа


