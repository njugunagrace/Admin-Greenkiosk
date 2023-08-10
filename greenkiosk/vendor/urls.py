from django.urls import path

from .views import edit_vendor_view, upload_vendor, vendor_detail, vendor_list

urlpatterns = [
    path("vendor/upload", upload_vendor, name="vendor_upload_view"),
    path("vendor/list", vendor_list , name ="vendor_list_view"),
    path("vendor/<int:id>/", vendor_detail, name= "vendor_details_view"),
    path("vendor/edit/<int:id>/", edit_vendor_view, name="vendor_edit_view"),
    ]