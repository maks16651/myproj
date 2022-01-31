from django.urls import path
from . import views # импортируем из этой же дирректории (. указывает что из этой же) файл views

urlpatterns = [
    path('',views.index , name = "home"),
    path('about',views.death, name = "about"),
    path('creating',views.creating, name = "creating"),
    path('themes',views.themes, name = "themes"),
    path('billy',views.billy, name = "billy"),
    path('login',views.Autorisation.as_view(), name = "login"),
    path('registration',views.Registration.as_view(), name = "registration")

]