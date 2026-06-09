# imports Django's Admin Panel and the Property model
from django.contrib import admin
from .models import Property, Contractor, MaintenanceJob

# Show the Property, Contractor, and MaintenanceJob models inside the Admin Panel
admin.site.register(Property)
admin.site.register(Contractor)
admin.site.register(MaintenanceJob)
