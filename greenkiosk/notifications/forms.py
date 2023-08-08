from django import forms
from .models import Notifications

class NotificationsUploadForm(forms.ModelForm):
    class Meta:
        model = Notifications
        fields = "__all__"