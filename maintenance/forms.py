from django import forms
from .models import Property, MaintenanceJob


class PropertyForm(forms.ModelForm):

    class Meta:
        model = Property
        fields = ['name', 'address']

class MaintenanceJobForm(forms.ModelForm):

    class Meta:
        model = MaintenanceJob

        fields = [
            'title',
            'description',
            'property',
            'contractor',
            'priority',
            'status',
        ]

        