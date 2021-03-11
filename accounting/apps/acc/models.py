from datetime import date

from django.db import models
from django.db.models import DecimalField


class Product(models.Model):
    name = models.CharField(max_length=255, blank=True)
    price = models.IntegerField()
    quantity = models.IntegerField()


class Service(models.Model):

    WATER_SUPPLY = 'Water'
    ELECTRICITY = 'Electricity'
    HEATING = 'Heating'
    SERVICE_CHOICES = [
        (HEATING, 'Отопление'),
        (WATER_SUPPLY, 'Вода'),
        (ELECTRICITY, 'Ток'),
    ]

    type_of_service = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    price = models.DecimalField(max_digits=8, decimal_places=5, null=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=5, null=True)
    starting_date = models.DateField(null=True)
    ending_date = models.DateField(null=True)

    def calculate_total(self):
        return DecimalField.to_python(self.price, self.price) * DecimalField.to_python(self.quantity, self.quantity)


class Student(models.Model):
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    GRADUATE = 'GR'
    YEAR_IN_SCHOOL_CHOICES = [
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        (GRADUATE, 'Graduate'),
    ]
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )
