from django.urls import path
from .views import cart_detail, edit_cart_view, upload_cart, view_cart

urlpatterns = [
    path("cart/view", view_cart, name="view_cart_view"),
    path("cart/upload", upload_cart, name="upload_cart_view" ),    
    path("cart/<int:id>/", cart_detail, name= "cart_details_view"),
    path("cart/edit/<int:id>/", edit_cart_view, name="cart_edit_view"),

]