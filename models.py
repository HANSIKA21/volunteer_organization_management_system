from django.db import models

class Organization(models.Model):
# Create your models here.
    name=models.CharField(max_length=500) 
    volunteer_organization_type=models.CharField(max_length=500, null=True)
    contact_number=models.CharField(max_length=50, null=True)
    desctiption=models.CharField(max_length=500, null=True)
def __str__(self):
        return self.name +""
# Create your models here.

class Organization_notification (models.Model):  
    name = models.CharField(max_length=50, null=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    desctiption=models.CharField(max_length=500, null=True)