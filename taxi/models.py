from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} {self.country}"
    

class Driver(AbstractUser):
    license_number = models.CharField(max_length=255)

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"
        ordering = ["id"]

    def __str__(self):
        return f"{self.username}"

    def get_absolute_url(self):
        return reverse("taxi:driver-detail", kwargs={'pk': self.pk})


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(Driver, related_name="cars")

    class Meta:
        ordering = ["manufacturer"]

    def __str__(self):
        return self.model

    def get_absolute_url(self):
        return reverse("taxi:car-detail", kwargs={'pk': self.pk})


class Trip(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
    license_number = models.ForeignKey(Driver, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("taxi:driver-salary", kwargs={'pk': self.pk})

    def __str__(self):
        return f"{self.created_at}"
