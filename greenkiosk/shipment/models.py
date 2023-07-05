from django.db import models

# Create your models here.
class Delivery(models.Model):
    date = models.DateTimeField()
    order = models.CharField(max_length=32)
    location = models.CharField(max_length=32)
    cost = models.DecimalField(max_digits=6 ,decimal_places=2)
    status = models.CharField(max_length=32)
    
    def __str__(self):
        return self.location