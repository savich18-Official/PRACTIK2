from django.contrib.auth.views import LogoutView
from django.http import HttpResponse

class CustomLogoutView(LogoutView):
    next_page = '/auth/login/'  # куда перекидывать после logout

def set_cookie_view(request):
    response = HttpResponse("Cookie установлена")
    response.set_cookie('mycookie', 'hello', max_age=3600)
    return response

def get_cookie_view(request):
    value = request.COOKIES.get('mycookie', 'Значение cookie не найдено')
    return HttpResponse(f'Cookie: {value}')

def set_session_view(request):
    request.session['mysession'] = 'session_value'
    return HttpResponse("Сессия установлена")

def get_session_view(request):
    value = request.session.get('mysession', 'Сессия пуста')
    return HttpResponse(f'Сессия: {value}')
