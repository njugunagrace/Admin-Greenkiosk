from django.shortcuts import render
from vendor.models import Vendor
from .forms import VendorUploadForm
from django.shortcuts import redirect

def upload_vendor(request):
    if request.method == "POST":
        form = VendorUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form =  VendorUploadForm()       
    return render(request, "vendor/vendor_upload.html", {"form": form})

def vendor_list(request):
    vendors = Vendor.objects.all()
    return render(request, "vendor/vendor_list.html", {"vendors": vendors})

def vendor_detail(request, id):
    vendor = Vendor.objects.get(id=id)
    return render(request, "vendor/vendor_details.html", {"vendor": vendor})

def edit_vendor_view(request, id):
    vendor = Vendor.objects.get(id = id)
    if request.method == 'POST':
        form = VendorUploadForm(request.POST, instance=vendor)
        if form.is_valid():
            form.save()
            return redirect("vendor_details_view", id = vendor.id)
    else:
        form = VendorUploadForm(instance= vendor)
        return render(request, "vendor/edit_vendor.html", {"form": form})



