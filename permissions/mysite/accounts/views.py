# accounts/views.py
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('accounts:login')

# Пример AboutMeView, если нужен:
from django.views.generic import TemplateView

class AboutMeView(TemplateView):
    template_name = 'accounts/about.html'
