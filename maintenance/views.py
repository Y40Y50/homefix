from django.shortcuts import render
from .models import Property, Contractor
from .forms import PropertyForm

def home(request):
    return render(request, 'maintenance/home.html')

def property_list(request):
    properties = Property.objects.all()

    return render(
        request,
        'maintenance/property_list.html',
        {'properties': properties}
    )
def contractor_list(request):
    contractors = Contractor.objects.all()

    return render(
        request,
        'maintenance/contractor_list.html',
        {'contractors': contractors}
    )

# View to create a new property
def create_property(request):

    form = PropertyForm()

    context = {
        'form': form
    }

    return render(
        request,
        'maintenance/create_property.html',
        context
    )