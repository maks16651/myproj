
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('MyWebsites.urls')) # показываем , что при переходе на главную страницу будет вызываться ффайл mywebsites.urls
]
