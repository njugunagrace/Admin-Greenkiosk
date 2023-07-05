from django.db import models

# Create your models here.
class Cart(models.Model):
    total_products = models.DecimalField(max_digits=6 ,decimal_places=2)
    number_of_products = models.PositiveIntegerField()
    payment_options = models.CharField(max_length=32)
    
    def __str__(self):
        return self.name