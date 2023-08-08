from django.urls import path
from .views import upload_cart, view_cart

urlpatterns = [
    path("products/view", view_cart, name="view_cart_view"),
    path("products/upload", upload_cart, name="upload_cart_view" ),
]