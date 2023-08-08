from django.urls import path
from .views import upload_notifications

urlpatterns = [
    path("produts/upload", upload_notifications, name="product_notifications_view")
]