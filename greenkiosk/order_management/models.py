from django.db import models
from payment.models import Payment
from cart.models import Cart
from customer.models import Customer


# Create your models here.

class Order(models.Model):
    date = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    cart = models.OneToOneField(Cart,models.PROTECT, null=True)
    payment = models.OneToOneField(Payment, models.PROTECT , null=True)
    delivery_options = models.CharField(max_length=32)
    delivery_date = models.DateTimeField()
     
    def __str__(self):
        return f"Order #{self.pk}"
