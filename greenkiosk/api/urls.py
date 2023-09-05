from django.urls import path
from .views import CartDetailView, CartListView, CustomerDetailView, CustomerListView, OrderDetailView, OrderListView, ProductDetailView, ProductListView

urlpatterns = [
    path("customers/", CustomerListView.as_view(), name="customer_list_view"),
    path ("customers/<int:id>",  CustomerDetailView.as_view(), name ="customer_detail_view"),

    path("products/", ProductListView.as_view(), name="product_list_view"),
    path ("products/<int:id>/",  ProductDetailView.as_view(), name ="product_detail_view"),

    path("orders/", OrderListView.as_view(), name="order_list_view"),
    path ("orders/<int:id>/",  OrderDetailView.as_view(), name ="order_detail_view"),

    path("cart/", CartListView.as_view(), name="cart_list_view"),
    path ("cart/<int:id>/",  CartDetailView.as_view(), name ="cart_detail_view"),
]