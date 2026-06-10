from django.shortcuts import render, redirect
from .models import Property, Contractor, MaintenanceJob
from .forms import PropertyForm, MaintenanceJobForm, ContractorForm
from django.contrib.auth.decorators import login_required

@login_required
def home(request):

    property_count = Property.objects.filter(
        user=request.user
    ).count()

    contractor_count = Contractor.objects.filter(
        user=request.user
    ).count()

    job_count = MaintenanceJob.objects.filter(
        user=request.user
    ).count()

    pending_jobs = MaintenanceJob.objects.filter(
        user=request.user,
        status='pending'
    ).count()

    in_progress_jobs = MaintenanceJob.objects.filter(
        user=request.user,
        status='in_progress'
    ).count()

    completed_jobs = MaintenanceJob.objects.filter(
        user=request.user,
        status='completed'
    ).count()

    context = {
        'property_count': property_count,
        'contractor_count': contractor_count,
        'job_count': job_count,
        'pending_jobs': pending_jobs,
        'in_progress_jobs': in_progress_jobs,
        'completed_jobs': completed_jobs,
    }

    return render(
        request,
        'maintenance/home.html',
        context
    )
@login_required
def property_list(request):

    properties = Property.objects.filter(
        user=request.user
    )

    return render(
        request,
        'maintenance/property_list.html',
        {'properties': properties}
    )


@login_required
def contractor_list(request):

    contractors = Contractor.objects.filter(
        user=request.user
    )

    return render(
        request,
        'maintenance/contractor_list.html',
        {'contractors': contractors}
    )
# View to create a new property
@login_required
def create_property(request):

    if request.method == 'POST':

        form = PropertyForm(request.POST)

        if form.is_valid():
            property = form.save(commit=False)
            property.user = request.user
            property.save()
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
@login_required
def delete_property(request, property_id):

    property = Property.objects.get(
        id=property_id,
        user=request.user
    )
    property.delete()

    return redirect('property_list')

# View to edit a property
@login_required
def edit_property(request, property_id):

    property = Property.objects.get(
        id=property_id,
        user=request.user
    )

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
@login_required
def job_list(request):

    jobs = MaintenanceJob.objects.filter(
    user=request.user
)

    context = {
        'jobs': jobs
    }

    return render(
        request,
        'maintenance/job_list.html',
        context
    )

# View to create a new maintenance job
@login_required
def create_job(request):

    if request.method == 'POST':
        form = MaintenanceJobForm(request.POST)

        # Only show this user's properties
        form.fields['property'].queryset = Property.objects.filter(
            user=request.user
        )
        form.fields['contractor'].queryset = Contractor.objects.filter(
            user=request.user
        )

        if form.is_valid():
            job = form.save(commit=False)
            job.user = request.user
            job.save()
            return redirect('job_list')

    else:
        form = MaintenanceJobForm()

        form.fields['property'].queryset = Property.objects.filter(
        user=request.user
        )

        form.fields['contractor'].queryset = Contractor.objects.filter(
        user=request.user
        )

    return render(
        request,
        'maintenance/create_job.html',
        {'form': form}
    )

@login_required
def delete_job(request, job_id):

    job = MaintenanceJob.objects.get(
        id=job_id,
        user=request.user
    )

    job.delete()

    return redirect('job_list')

@login_required
def edit_job(request, job_id):

    job = MaintenanceJob.objects.get(
        id=job_id,
        user=request.user
    )
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

# View to create a new contractor
@login_required
def create_contractor(request):

    if request.method == 'POST':

        form = ContractorForm(request.POST)

        if form.is_valid():
            contractor = form.save(commit=False)
            contractor.user = request.user
            contractor.save()
            return redirect('contractor_list')

    else:

        form = ContractorForm()

    context = {
        'form': form
    }

    return render(
        request,
        'maintenance/create_contractor.html',
        context
    )
# View to delete a contractor

@login_required
def delete_contractor(request, contractor_id):

    contractor = Contractor.objects.get(
    id=contractor_id,
    user=request.user
)
    contractor.delete()

    return redirect('contractor_list')

@login_required
def edit_contractor(request, contractor_id):

    contractor = Contractor.objects.get(
    id=contractor_id,
    user=request.user
)

    if request.method == 'POST':

        form = ContractorForm(
            request.POST,
            instance=contractor
        )

        if form.is_valid():

            form.save()

            return redirect('contractor_list')

    else:

        form = ContractorForm(
            instance=contractor
        )

    context = {
        'form': form
    }

    return render(
        request,
        'maintenance/edit_contractor.html',
        context
    )
