from django.contrib import admin
from .models import Customer

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name","phone_number","email","address","date_created")

admin.site.register(Customer , CustomerAdmin)    
