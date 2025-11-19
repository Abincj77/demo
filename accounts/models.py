
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  # <-- THIS FIXES THE ERROR
    bio = models.TextField(max_length=500, blank=True)
    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['username'] # Required when creating a user via createsuperuser
