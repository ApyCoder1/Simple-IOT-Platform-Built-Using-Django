from django.contrib.auth.models import User
from django.db import models

class Device(models.Model):
    device_name = models.CharField(max_length=100, unique=True)  # Device identifier
    api_key = models.CharField(max_length=255, unique=True)  # API key for authentication
    led1_status = models.BooleanField(default=False)
    led2_status = models.BooleanField(default=False)
    led3_status = models.BooleanField(default=False)
    led4_status = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to User model

    def __str__(self):
        return f"Device: {self.device_name}, API Key: {self.api_key}, " \
               f"LED1: {'ON' if self.led1_status else 'OFF'}, " \
               f"LED2: {'ON' if self.led2_status else 'OFF'}, " \
               f"LED3: {'ON' if self.led3_status else 'OFF'}, " \
               f"LED4: {'ON' if self.led4_status else 'OFF'}, " \
               f"User: {self.user.username}"
