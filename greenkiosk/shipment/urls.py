from django.urls import path
from .views import delivery_detail, delivery_list, edit_delivery_view, upload_delivery

urlpatterns = [
    path("delivery/upload", upload_delivery, name="delivery_upload_view"),
    path("delivery/list", delivery_list , name ="delivery_list_view"),
    path("delivery/<int:id>/", delivery_detail, name= "delivery_details_view"),
    path("delivery/edit/<int:id>/", edit_delivery_view, name="delivery_edit_view"),
    ]