from django.urls import path
from .views import edit_order_view, order_detail, orders_list, upload_order


urlpatterns = [
    path("orders/upload", upload_order , name="order_upload_view"),
    path("orders/list", orders_list, name="order_list_view"),
    path("orders/<int:id>/", order_detail, name="order_details_view"),
    path("orders/edit/<int:id>/", edit_order_view, name="order_edit_view"),
]