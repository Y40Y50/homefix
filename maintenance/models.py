# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Creating a Model for Property
class Property(models.Model):
    PROPERTY_TYPES = [
        ('house', 'House'),
        ('flat', 'Flat'),
        ('bungalow', 'Bungalow'),
        ('other', 'Other'),
    ]
# Foreign Key for table relationship with User
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
# Basic details about the property
    name = models.CharField(max_length=100)
    address = models.TextField()
    property_type = models.CharField(
        max_length=20,
        choices=PROPERTY_TYPES
    )
# Automatically records when the property was created
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
# Creating the Contractor Table 
class Contractor(models.Model):
    TRADE_TYPES = [
        ('plumber', 'Plumber'),
        ('electrician', 'Electrician'),
        ('carpenter', 'Carpenter'),
        ('painter', 'Painter'),
        ('other', 'Other'),
    ]
    # Stores the contractor's name
    name = models.CharField(max_length=100)
    trade_type = models.CharField(
        max_length=20,
        choices=TRADE_TYPES
    )
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name
    