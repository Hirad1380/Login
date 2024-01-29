from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.



class CustomUser(AbstractUser):
    security = models.CharField(max_length=100)
    password_history=models.ManyToManyField("PasswordHistory", blank=True)
    



class PasswordHistory(models.Model):
    password=models.CharField(max_length=128)
    

    