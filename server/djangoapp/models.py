from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator

class CarMake(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    country = models.CharField(max_length=50, blank=True)  # Optional extra field

    def __str__(self):
        return self.name


class CarModel(models.Model):
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'
    COUPE = 'Coupe'
    HATCHBACK = 'Hatchback'
    TRUCK = 'Truck'

    CAR_TYPE_CHOICES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
        (COUPE, 'Coupe'),
        (HATCHBACK, 'Hatchback'),
        (TRUCK, 'Truck'),
    ]

    make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name='models')
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=CAR_TYPE_CHOICES, default=SEDAN)
    year = models.IntegerField(validators=[MinValueValidator(2015), MaxValueValidator(2023)])
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Optional
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.make.name} {self.name} ({self.year})"
