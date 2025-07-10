from django.urls import path, include
from .views import driver_dashboard

app_name = 'driver'

urlpatterns = [
    path('dashboard/', driver_dashboard, name='dashboard'),
]
