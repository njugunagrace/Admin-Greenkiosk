from django.db import models
from inventory.models import Product


class Cart(models.Model):
    products = models.ManyToManyField(Product)
    total_products = models.DecimalField(max_digits=6 ,decimal_places=2)
    number_of_products = models.PositiveIntegerField()
    payment_options = models.CharField(max_length=32)
    
    def __str__(self):
        return f"Cart #{self.pk}"
    
    def add_product(self , product):
        self.products.add(product)
        self.save()
        return self
    
    def products_total(self):
        products = self.products
        total = 0
        for product in products:
            total += product.price
        return total    

    