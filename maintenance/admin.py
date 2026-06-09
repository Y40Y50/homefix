# imports Django's Admin Panel and the Property model
from django.contrib import admin
from .models import Property, Contractor

# Show the Property and Contractor models inside the Admin Panel
admin.site.register(Property)
admin.site.register(Contractor)
