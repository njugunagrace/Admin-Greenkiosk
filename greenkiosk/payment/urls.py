from django.urls import path

from .views import edit_payment_view, payment_detail, payment_list, upload_payment

urlpatterns = [
    path("payment/upload", upload_payment, name="payment_upload_view"),
    path("payment/list", payment_list , name ="payment_list_view"),
    path("payment/", payment_detail, name= "payment_details_view"),
    path("payment/edit/<int:id>/", edit_payment_view, name="payment_edit_view"),
]