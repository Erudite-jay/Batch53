from django.db import models

# Create your models here.

class Contact(models.Model):
    full_name=models.CharField(max_length=120)
    phone=models.CharField(max_length=10)
    email=models.EmailField(max_length=30)
    country=models.CharField(max_length=20)
