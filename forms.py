from django.forms import ModelForm, Form
from app.models import Organization
from app.models import Organization_notification
from django import forms



class OrganizationForm(ModelForm):
    class Meta:
        model = Organization
        fields = "__all__"

class Organization_notificationForm(ModelForm):
    class Meta:
        model = Organization_notification
        fields = "__all__"