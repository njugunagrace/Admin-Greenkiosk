from django.shortcuts import render
from .forms import NotificationsUploadForm

def upload_notifications(request):
    if request.method == "POST":
        form = NotificationsUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form =  NotificationsUploadForm()       
    return render(request, "notifications/notifications_upload.html", {"form": form})