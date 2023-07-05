from django.contrib import admin
from .models import Cart

# Register your models here.

class CartAdmin(admin.ModelAdmin):
    list_display = ("total_products","number_of_products","payment_options")

admin.site.register(Cart, CartAdmin)
