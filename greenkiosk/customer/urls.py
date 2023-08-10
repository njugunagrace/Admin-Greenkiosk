from django.urls import path
from .views import customer_detail, customer_list, upload_customer


urlpatterns = [
    path("customers/upload", upload_customer, name="customer_upload_view"),
    path("customers/list", customer_list, name="customer_list_view" ),
    path("customers/detail", customer_detail, name="customer_detail_view"),
    
]