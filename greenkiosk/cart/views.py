from django.shortcuts import render
from .models import Cart
from .forms import CartItemForm
from django.shortcuts import redirect

def upload_cart(request):
    if request.method == "POST":
        form = CartItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form =  CartItemForm()       
    return render(request, "cart/upload_cart.html", {"form": form})

def view_cart(request):
    carts = Cart.objects.all()
    return render(request, "cart/view_cart.html", {"carts": carts})

def cart_detail(request, id):
    cart = Cart.objects.get(id=id)
    return render(request, "cart/cart_details.html", {"cart": cart})

def edit_cart_view(request, id):
    cart = Cart.objects.get(id = id)
    if request.method == 'POST':
        form = CartItemForm(request.POST, instance=cart)
        if form.is_valid():
            form.save()
            return redirect("payment_details_view", id = cart.id)
    else:
        form = CartItemForm(instance= cart)
        return render(request, "payment/edit_cart.html", {"form": form})

