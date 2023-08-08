from django.contrib import admin
from .models import Delivery

# Register your models here.

class DeliveryAdmin(admin.ModelAdmin):
    list_display = ("date","location","cost","status")
admin.site.register(Delivery, DeliveryAdmin)    
    
