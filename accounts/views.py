from django.shortcuts import render
from django.contrib.auth.views import LoginView as BaseLoginView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from .forms import EmailLoginForm, CustomUserCreationForm

User = get_user_model()


class LoginView(BaseLoginView):
    form_class = EmailLoginForm
    template_name = 'accounts/login.html'

    def get_success_url(self):
        user = self.request.user
        if user.role == 'driver':
            return reverse_lazy('driver:dashboard')
        elif user.role == 'company':
            return reverse_lazy('accounts:dashboard')
        else:
            return reverse_lazy('admin:index')


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')


@login_required
def company_dashboard(request):
    return render(request, 'accounts/dashboard.html')
