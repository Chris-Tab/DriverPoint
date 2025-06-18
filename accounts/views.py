from django.shortcuts import render

from django.contrib.auth.views import LoginView as BaseLoginView
from django.urls import reverse_lazy
from .forms import EmailLoginForm
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
user = get_user_model()

class LoginView(BaseLoginView):
    form_class = EmailLoginForm
    template_name = 'accounts/login.html'

    def get_success_url(self):
        user = self.request.user
        if user.role == 'driver':
            return reverse_lazy('driver:dashboard')
        elif user.role == 'company':
            return reverse_lazy('company:dashboard')
        else:
            return reverse_lazy('admin:index')  # default to admin panel


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')