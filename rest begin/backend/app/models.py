from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=150)
    body = models.CharField(max_length=150)
    
    def __str__(self):
        return self.title