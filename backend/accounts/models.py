# accounts/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=64, unique=True)

    # Add custom fields here, if needed

    def __str__(self):
        return self.username