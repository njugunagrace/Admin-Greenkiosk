from django.shortcuts import render
from shipment.models import Delivery
from .forms import DeliveryUploadForm
from django.shortcuts import redirect

def upload_delivery(request):
    if request.method == "POST":
        form = DeliveryUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form =  DeliveryUploadForm()       
    return render(request, "shipment/delivery_upload.html", {"form": form})

def delivery_list(request):
    deliveries = Delivery.objects.all()
    return render(request, "shipment/delivery_list.html", {"deliveries": deliveries})

def delivery_detail(request, id):
    delivery = Delivery.objects.get(id=id)
    return render(request, "shipment/delivery_details.html", {"delivery": delivery})

def edit_delivery_view(request, id):
    delivery = Delivery.objects.get(id = id)
    if request.method == 'POST':
        form = DeliveryUploadForm(request.POST, instance=delivery)
        if form.is_valid():
            form.save()
            return redirect("delivery_details_view", id = delivery.id)
    else:
        form = DeliveryUploadForm(instance= delivery)
        return render(request, "shipment/edit_delivery.html", {"form": form})
