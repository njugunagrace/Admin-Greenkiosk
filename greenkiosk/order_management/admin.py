from django.contrib import admin
from .models import Order

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display =("date","delivery_options","delivery_date")
    
admin.site.register(Order,OrderAdmin)   
    