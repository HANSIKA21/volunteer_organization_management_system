from django.shortcuts import render
from app.models import Organization
from app.models import Organization_notification
from django.shortcuts import redirect
from django.http import HttpResponse
from app.forms import OrganizationForm
from app.forms import Organization_notificationForm

def organization (request):
    organizations = Organization.objects.all  ()
    form = OrganizationForm()
    context = {'objects' :organizations , 'form':form}; #make a dictionary
    return render(request, 'organization.html',context)
# Create your views here.

def organization_notification (request):
    organization_notifications = Organization_notification.objects.all  ()
    form = Organization_notificationForm()
    context = {'objects' :organization_notifications ,'form':form}; #make a dictionary
    return render(request, 'Organization_notification.html',context)

def organization_add (request):
    form = OrganizationForm(request.GET)
    if form.is_valid():
        form.save()
        return redirect('organization')
    return HttpResponse("Form is not valid")

    
def organization_delete (request, id):
    organization = Organization.objects.get(pk=id)
    organization.delete()
    return redirect('organization')

def organization_view (request, id):
    organization = Organization.objects.get(pk=id)
    context = {
        'object':organization
    }
    return render(request, 'Organization2.html', context)

def organization_notification_add (request):
    form =  Organization_notificationForm(request.GET)
    if form.is_valid():
        form.save()
        return redirect('organization_notification')
    return HttpResponse("Form is not valid")

    
def organization_notification_delete (request, id):
    organization_notification =  Organization_notification.objects.get(pk=id)
    organization_notification.delete()
    return redirect(' Organization_notification')

def organization_notification_view (request, id):
    organization_notification =  Organization_notification.objects.get(pk=id)
    context = {
        'object': organization_notification
    }
    return render(request, 'organization_notification2.html', context)

