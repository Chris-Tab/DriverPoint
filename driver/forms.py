from django import forms
from .models import DriverProfile

class DriverProfileForm(forms.ModelForm):
    class Meta:
        model = DriverProfile
        fields = ['full_name', 'phone_number', 'license_number', 'address']
