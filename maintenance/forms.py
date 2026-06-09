from django import forms
from .models import Property, MaintenanceJob, Contractor


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


class ContractorForm(forms.ModelForm):

    class Meta:
        model = Contractor

        fields = [
            'name',
            'trade_type',
            'phone',
            'email',
        ]
        