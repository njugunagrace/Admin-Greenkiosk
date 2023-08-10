from django.shortcuts import render
from payment.models import Payment
from .forms import PaymentUploadForm
from django.shortcuts import redirect

def upload_payment(request):
    if request.method == "POST":
        form = PaymentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form =  PaymentUploadForm()       
    return render(request, "payment/payment_upload.html", {"form": form})

def payment_list(request):
    payments = Payment.objects.all()
    return render(request, "payment/payment_list.html", {"payments": payments})

def payment_detail(request, id):
    payment = Payment.objects.get(id=id)
    return render(request, "payment/payment_details.html", {"payment": payment})

def edit_payment_view(request, id):
    payment = Payment.objects.get(id = id)
    if request.method == 'POST':
        form = PaymentUploadForm(request.POST, instance=payment)
        if form.is_valid():
            form.save()
            return redirect("payment_details_view", id = payment.id)
    else:
        form = PaymentUploadForm(instance= payment)
        return render(request, "payment/edit_payment.html", {"form": form})


