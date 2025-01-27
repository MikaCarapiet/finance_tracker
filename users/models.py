from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True) #Auto-generate creation timestamp

    # Use email as the unique identifier for authentication
    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email' # Use email to login to account

    def __str__(self):
        return f"{self.last_name.upper()}, {self.first_name}"
