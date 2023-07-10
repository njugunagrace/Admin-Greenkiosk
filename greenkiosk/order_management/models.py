from django.db import models
from payment.models import Payment

# Create your models here.

class Order(models.Model):
    payment = models.OneToOneField(Payment, models.PROTECT , null=True)
    customers = models.CharField(max_length=32)
    date = models.DateField()
    products = models.CharField(max_length=32)
    delivery_options = models.CharField(max_length=32)
    delivery_date = models.DateTimeField()
     
    def __str__(self):
        return self.customers 
