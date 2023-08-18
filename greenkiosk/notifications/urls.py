from django.urls import path
from .views import edit_notifications_view, notifications_detail, notifications_list, upload_notifications

urlpatterns = [
    path("notification/upload", upload_notifications, name="product_notifications_view"),
    path("notification/list", notifications_list, name="list_notifications_view"),
    path("notification/<int:id>/", notifications_detail, name="notifications_details_view"),
    path("notification/edit/<int:id>/", edit_notifications_view, name="notifications_edit_view"),
    ]