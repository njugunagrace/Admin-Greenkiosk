from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=32)
    phone_number = models.CharField(max_length=32)
    email = models.EmailField()
    address = models.CharField(max_length=32)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
