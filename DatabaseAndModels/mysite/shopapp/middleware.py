import time
from django.http import HttpResponseTooManyRequests

VISITS = {}

class ThrottleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR', '')
        now = time.time()
        last_visit = VISITS.get(ip, 0)
        if now - last_visit < 1:
            return HttpResponseTooManyRequests("Слишком много запросов. Подождите немного.")
        VISITS[ip] = now
        return self.get_response(request)
