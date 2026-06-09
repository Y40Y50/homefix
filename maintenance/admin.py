# imports Django's Admin Panel and the Property model
from django.contrib import admin
from .models import Property

# Show the Property model inside the Admin Panel
admin.site.register(Property)
