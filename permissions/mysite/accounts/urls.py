# accounts/urls.py
from django.urls import path
from .views import RegisterView, AboutMeView
from django.contrib.auth import views as auth_views

app_name = "accounts"  # Использование пространства имен

urlpatterns = [
    # Маршрут для страницы "О себе"
    path('about/', AboutMeView.as_view(), name='about_me'),

    # Маршрут для страницы регистрации
    path('register/', RegisterView.as_view(), name='register'),

    # Стандартные маршруты для логина и логаута
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

