from django.db import models

# Create your models here.

class Payment(models.Model):
    status = models.CharField(max_length=32)
    amount = models.DecimalField(max_digits=6 ,decimal_places=2)
    receipt = models.CharField(max_length=32)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.status
