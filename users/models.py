from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = [
        ("ADMIN", "Admin"),
        ("TECHNICIAN", "Technician"),
        ("SRM AGENT", "SRM Agent"),
        ("CITIZEN", "Citizen"),
    ]

    phone = models.CharField(max_length=20, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="CITIZEN")
