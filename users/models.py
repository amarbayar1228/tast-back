from django.db import models

# Create your models here.

class Users(models.Model):
    id = models.AutoField(primary_key=True) 
    lastName = models.CharField(max_length=500)
    firstName = models.CharField(max_length=500)
    gmail = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    description = models.CharField(max_length=500)