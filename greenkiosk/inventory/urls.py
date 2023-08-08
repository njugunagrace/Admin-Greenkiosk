from django.urls import path
from .views import edit_product_view, product_detail, products_list, upload_product

urlpatterns = [
    path("products/upload", upload_product, name="product_upload_view"),
    path("products/list", products_list , name ="product_list_view"),
    path("products/<int:id>/", product_detail, name= "product_details_view"),
    path("products/edit/<int:id>/", edit_product_view, name="product_edit_view"),
    ]