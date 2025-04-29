from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from shopapp.views import upload_file_view

def index(request):
    return HttpResponse("Главная страница работает!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('upload/', upload_file_view),  # ← добавь этот маршрут
]
