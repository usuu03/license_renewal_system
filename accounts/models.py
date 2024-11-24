from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    organization = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return f"{self.email} from {self.organization}"