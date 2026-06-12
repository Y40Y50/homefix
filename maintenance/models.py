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

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    name = models.CharField(max_length=100)
    address = models.TextField()

    property_type = models.CharField(
        max_length=20,
        choices=PROPERTY_TYPES
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Creating the Contractor Table
from django.core.validators import RegexValidator

phone_validator = RegexValidator(
    regex=r'^\+?[\d\s()-]{7,20}$',
    message='Enter a valid phone number.'
)

class Contractor(models.Model):

    TRADE_TYPES = [
        ('plumber', 'Plumber'),
        ('electrician', 'Electrician'),
        ('carpenter', 'Carpenter'),
        ('painter', 'Painter'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    name = models.CharField(max_length=100)

    trade_type = models.CharField(
        max_length=20,
        choices=TRADE_TYPES
    )

    phone = models.CharField(
        max_length=20,
        validators=[phone_validator]
    )

    email = models.EmailField()

    def __str__(self):
        return self.name

class MaintenanceJob(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    PRIORITY_CHOICES = [
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE
    )

    contractor = models.ForeignKey(
        Contractor,
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=100)

    description = models.TextField()

    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
