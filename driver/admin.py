from django.contrib import admin
from .models import DriverProfile

@admin.register(DriverProfile)
class DriverProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'user', 'phone_number', 'license_number')
