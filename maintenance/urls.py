from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('properties/', views.property_list, name='property_list'),
    path('contractors/', views.contractor_list, name='contractor_list'),
    path('properties/create/', views.create_property, name='create_property'),
    path(
    'properties/delete/<int:property_id>/',
    views.delete_property,
    name='delete_property'
),
    path(
    'properties/edit/<int:property_id>/',
    views.edit_property,
    name='edit_property'
),
    path('jobs/', views.job_list, name='job_list'),
    path('jobs/create/', views.create_job, name='create_job'),
    path('jobs/delete/<int:job_id>/', views.delete_job, name='delete_job'),
    path('jobs/edit/<int:job_id>/', views.edit_job, name='edit_job'),
    path(
    'contractors/create/',
    views.create_contractor,
    name='create_contractor'
),
path(
    'contractors/delete/<int:contractor_id>/',
    views.delete_contractor,
    name='delete_contractor'
),
path(
    'contractors/edit/<int:contractor_id>/',
    views.edit_contractor,
    name='edit_contractor'
),

]