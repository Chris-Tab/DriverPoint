from django.urls import path
from .views import driver_dashboard, driver_profile, create_driver_profile

app_name = 'driver'

urlpatterns = [
    path('dashboard/', driver_dashboard, name='dashboard'),
    path('profile/', driver_profile, name='profile'),
    path('create-profile/', create_driver_profile, name='create_profile'),
]
