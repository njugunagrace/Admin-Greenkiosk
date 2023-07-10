from django.db import models
from customer.models import Customer

# Create your models here.
class Notifications(models.Model):
    message = models.CharField(max_length=32)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    time = models.DateTimeField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.message
    
    
