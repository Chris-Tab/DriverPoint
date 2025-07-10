from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class DriverProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    license_number = models.CharField(max_length=50)
    address = models.TextField(blank=True)

    def __str__(self):
        return f"{self.full_name} ({self.user.email})"
