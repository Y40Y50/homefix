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
]