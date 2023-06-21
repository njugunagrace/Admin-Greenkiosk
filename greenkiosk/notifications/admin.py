from django.contrib import admin
from .models import Notifications

# Register your models here.
class NotificationsAdmin(admin.ModelAdmin):
    list_display = ("message","time","date_created")

admin.site.register(Notifications,NotificationsAdmin)   
