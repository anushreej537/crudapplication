from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.IntegerField()
    password = models.CharField(max_length=255)
    
    
