from django.shortcuts import render, redirect
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

    if request.method == 'POST':

        form = PropertyForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('property_list')

    else:
        form = PropertyForm()

    context = {
        'form': form
    }

    return render(
        request,
        'maintenance/create_property.html',
        context
    )
# View to delete a property
def delete_property(request, property_id):

    property = Property.objects.get(id=property_id)

    property.delete()

    return redirect('property_list')