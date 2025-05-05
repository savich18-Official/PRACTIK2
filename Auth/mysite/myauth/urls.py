from django.urls import path
from django.contrib.auth.views import LoginView
from .views import CustomLogoutView, set_cookie_view, get_cookie_view, set_session_view, get_session_view

urlpatterns = [
    path('login/', LoginView.as_view(
        template_name='myauth/login.html',
        redirect_authenticated_user=True
    ), name='login'),

    path('logout/', CustomLogoutView.as_view(), name='logout'),

    path('set-cookie/', set_cookie_view, name='set_cookie'),
    path('get-cookie/', get_cookie_view, name='get_cookie'),

    path('set-session/', set_session_view, name='set_session'),
    path('get-session/', get_session_view, name='get_session'),
]
