from django.shortcuts import render
from order_management.models import Order
from .forms import OrderUploadForm
from django.shortcuts import redirect

def upload_order(request):
    if request.method == "POST":
        form = OrderUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form =  OrderUploadForm()       
    return render(request, "order_management/order_upload.html", {"form": form})

def orders_list(request):
    orders = Order.objects.all()
    return render(request, "order_management/order_list.html", {"orders": orders})

def order_detail(request, id):
    order = Order.objects.get(id=id)
    return render(request, "order_management/order_details.html", {"order": order})

def edit_order_view(request, id):
    order = Order.objects.get(id = id)
    if request.method == 'POST':
        form = OrderUploadForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect("order_details_view", id = order.id)
    else:
        form = OrderUploadForm(instance= order)
        return render(request, "order_management/edit_order.html", {"form": form})