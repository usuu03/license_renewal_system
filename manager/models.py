from django.db import models
from django.contrib.auth.models import AbstractUser

LICENSE_TYPE_CHOICES = [
        ('Software', 'Software'),
        ('Hardware', 'Hardware'),
    ]
# Create your models here.
class License(models.Model):
    name = models.CharField(max_length=255)
    license_type = models.CharField(max_length=255, choices=LICENSE_TYPE_CHOICES)
    vendor = models.CharField(max_length=255)
    license_key = models.CharField(max_length=255, unique=True)
    pucharse_date = models.DateField()
    expiration_date = models.DateField()
    renewal_terms = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name