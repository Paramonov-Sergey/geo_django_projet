from django.db import models
from django.urls import reverse


class Measurements(models.Model):
    location = models.CharField(max_length=200)  # ip address
    destination = models.CharField(max_length=200)
    distance = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Distance from {self.location} to {self.destination} is {self.distance} km'

    def get_absolute_url(self):
        return reverse('measurements:view_map', kwargs={'pk': self.pk})
