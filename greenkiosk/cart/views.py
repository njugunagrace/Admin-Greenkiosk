from django.shortcuts import render
from .models import Cart
from .forms import CartItemForm

def upload_cart(request):
    if request.method == "POST":
        form = CartItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form =  CartItemForm()       
    return render(request, "cart/upload_cart.html", {"form": form})

def view_cart(request):
    products = Cart.objects.all()
    return render(request, "cart/view_cart.html", {"products": products})

