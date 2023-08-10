from django.shortcuts import render
from notifications.models import Notifications
from .forms import NotificationsUploadForm
from django.shortcuts import redirect

def upload_notifications(request):
    if request.method == "POST":
        form = NotificationsUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form =  NotificationsUploadForm()       
    return render(request, "notifications/notifications_upload.html", {"form": form})



def notifications_list(request):
    notifications = Notifications.objects.all()
    return render(request, "notifications/notifications_list.html", {"notifications": notifications})

def notifications_detail(request, id):
    notification = Notifications.objects.get(id=id)
    return render(request, "notifications/notifications_details.html", {"notification": notification})

def edit_notifications_view(request, id):
    notification = Notifications.objects.get(id = id)
    if request.method == 'POST':
        form = NotificationsUploadForm(request.POST, instance=notification)
        if form.is_valid():
            form.save()
            return _redirect ("notification_details_view", id = notification.id)
    else:
        form = NotificationsUploadForm(instance= notification)
        return render(request, "notifications/edit_notifications.html", {"form": form})

