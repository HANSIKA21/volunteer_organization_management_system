
from django.contrib import admin
from django.urls import path , include
from app import views

urlpatterns = [
    #path('admin/', admin.site.urls),
   # path('app/',include('app.urls'))
   path('organization/',views.organization, name='organization'),
   path('organization_notification/',views.organization_notification, name='organization_notification'),
   path('organization/add/',views.organization_add),
   path('organization/view/<int:id>',views.organization_view),
   path('organization/delete/<int:id>',views.organization_delete),
   path('organization_notification/add/',views.organization_notification_add),
   path('organization_notification/view/<int:id>',views.organization_notification_view),
   path('organization_notification/delete/<int:id>',views.organization_notification_delete),
]
