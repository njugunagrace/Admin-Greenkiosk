from customer.models import Customer
from inventory.models import Product
from order_management.models import Order
from cart.models import Cart
from rest_framework import serializers

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields =  "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"



class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many = True)
    class Meta:
        model = Cart
        fields = '__all__'        


