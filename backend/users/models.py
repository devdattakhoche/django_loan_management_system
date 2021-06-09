from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):

    roles = [("Admin", "Admin"), ("Agent", "Agent"), ("Customer", "Customer")]

    role = models.CharField(choices=roles, default="Customer", max_length=20)
    pass
