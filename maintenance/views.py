from django.shortcuts import render, redirect
from .models import Property, Contractor, MaintenanceJob
from .forms import PropertyForm, MaintenanceJobForm

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

# View to edit a property
def edit_property(request, property_id):

    property = Property.objects.get(id=property_id)

    if request.method == 'POST':

        form = PropertyForm(
            request.POST,
            instance=property
        )

        if form.is_valid():
            form.save()
            return redirect('property_list')

    else:

        form = PropertyForm(
            instance=property
        )

    context = {
        'form': form
    }

    return render(
        request,
        'maintenance/edit_property.html',
        context
    )
# View to list all maintenance jobs
def job_list(request):

    jobs = MaintenanceJob.objects.all()

    context = {
        'jobs': jobs
    }

    return render(
        request,
        'maintenance/job_list.html',
        context
    )

# View to create a new maintenance job
def create_job(request):

    if request.method == 'POST':

        form = MaintenanceJobForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('job_list')

    else:

        form = MaintenanceJobForm()

    context = {
        'form': form
    }

    return render(
        request,
        'maintenance/create_job.html',
        context
    )

def delete_job(request, job_id):

    job = MaintenanceJob.objects.get(id=job_id)

    job.delete()

    return redirect('job_list')

def edit_job(request, job_id):

    job = MaintenanceJob.objects.get(id=job_id)

    if request.method == 'POST':

        form = MaintenanceJobForm(
            request.POST,
            instance=job
        )

        if form.is_valid():

            form.save()

            return redirect('job_list')

    else:

        form = MaintenanceJobForm(
            instance=job
        )

    context = {
        'form': form
    }

    return render(
        request,
        'maintenance/edit_job.html',
        context
    )
