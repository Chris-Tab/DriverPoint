from django.urls import path
from .views import LoginView, RegisterView, company_dashboard
from django.contrib.auth.views import LogoutView


app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='accounts:login'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('dashboard/', company_dashboard, name='dashboard'),
]
