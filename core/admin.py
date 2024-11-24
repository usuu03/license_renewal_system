from django.contrib import admin
from .models import User, License

# Register your models here.
admin.site.register(User)
admin.site.register(License)