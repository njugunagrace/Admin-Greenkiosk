from .serializers import CustomerSerializer
from .serializers import ProductSerializer
from .serializers import OrderSerializer
from .serializers import CartSerializer
from rest_framework.views import APIView
from customer.models import Customer
from inventory.models import Product
from order_management.models import Order
from cart.models import Cart
from rest_framework.response import Response
from rest_framework import status

class CustomerListView(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many= True)
        return Response(serializer.data)   

    def post(self, request):
        serializer = CustomerSerializer(data = request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_created)
        
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class CustomerDetailView(APIView):
    def get(self, request, id, format = None) :
        customer = Customer.objects.get(id = id)   
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    
    def put(self , request , id , format = None):
        customer = Customer.objects.get(id = id)
        serializer = CustomerSerializer (customer, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data ,status = status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format = None):
        customer = Customer.objects.get(id = id)
        customer.delete()
        return Response("customer deleted" , status = status.HTTP_204_CONTENT_DELETE_) 
    

    

class ProductListView(APIView):
    def get(self , request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many= True)
        return Response(serializer.data)   

    def post(self, request):
        serializer = ProductSerializer(data = request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_created)
        
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class ProductDetailView(APIView):
    def get(self, request, id, format = None) :
        product = Product.objects.get(id = id)   
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def put(self , request , id , format = None):
        product = Product.objects.get(id = id)
        serilizer = ProductSerializer (product, request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data ,status = status.HTTP_201_CREATED)   
        return Response(serilizer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format = None):
        product = Product.objects.get(id = id)
        product.delete()
        return Response("product deleted" , status = status.HTTP_204_CONTENT_DELETE_) 





class OrderListView(APIView):
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders , many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status - status.HTTP_201_created)    
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class OrderDetailView(APIView):
    def get(self, request, id, format = None) :
        order = Order.objects.get(id = id)   
        serializer = OrderSerializer(order)
        return Response(serializer.data)
    
    def put(self , request , id , format = None):
        order = Order.objects.get(id = id)
        serializer = OrderSerializer (order, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data ,status = status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format = None):
        order = Order.objects.get(id = id)
        order.delete()
        return Response("order deleted" , status = status.HTTP_204_CONTENT_DELETE_) 
    


class CartListView(APIView):
    def get(self, request):
        cart = Cart.objects.all()
        serializer = CartSerializer(cart , many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CartSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status - status.HTTP_201_created)    
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class AddToCartView(APIView):
    def get(self, request, id, format=None):
        cart = Cart.objects.get(id=id)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    def post(self, request, format=None):
        cart_id = request.date["cart_id"]
        product_id = request.data["product_id"]
        product = Product.objects.get(id=product_id)
        cart = Cart.objects.get(id=cart_id)
        updated_cart= cart.add_product(product)
        serializer = CartSerializer(updated_cart)
        return Response(serializer.data)
    

    # def add_to_cart(self, request, id, product_id):
    #     cart = Cart.objects.get(id=id)
    #     product = Product.objects.get(id=product_id)
    #     cart.products.add(product)
    #     cart.save()
    #     serializer = CartSerializer(cart)
    #     return Response(serializer.data, status=status.HTTP_200_OK)    


    

    


