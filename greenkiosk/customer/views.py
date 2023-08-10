from django.shortcuts import render
from customer.models import Customer
from .forms import CustomerUploadForm

def upload_customer(request):
    if request.method == "POST":
        form = CustomerUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = CustomerUploadForm()
    return render(request, "customer/customer_upload.html", {"form" : form})

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, "customer/customer_list.html", {"customers": customers})

def customer_detail(request):
    customer = Customer.objects.get(id = id)
    return render(request, "customer/customer_details.html", {"customer" : customer})








