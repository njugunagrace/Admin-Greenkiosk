from django.db import models
from order_management.models import Order

# Create your models here.
class Delivery(models.Model):
    orders= models.OneToOneField(Order, models.PROTECT, null=True)
    date = models.DateTimeField()
    location = models.CharField(max_length=32)
    cost = models.DecimalField(max_digits=6 ,decimal_places=2)
    status = models.CharField(max_length=32)
    
    def __str__(self):
        return f"Order #{self.pk}"
    