from django.contrib import admin
from .models import Task # импортируем таск для создания базы данных

# Register your models here.
admin.site.register(Task) # рагистрируем модель таск в бд
