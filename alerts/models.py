from django.db import models
from django.contrib.auth.models import User

class Location(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name
class DisasterAlert(models.Model):
    SEVERITY_CHOICES = [
        ('low', 'Low'),
        ('moderate', 'Moderate'),
        ('high', 'High'),
        ('severe', 'Severe'),
        ('extreme', 'Extreme'),
    ]
class DisasterAlert(models.Model):
    ALERT_TYPES = [
        ('earthquake', 'Earthquake'),
        ('flood', 'Flood'),
        ('fire', 'Fire'),
        ('tsunami', 'Tsunami'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='alerts_disaster_alerts')  # Nom unique pour éviter les conflits
    type = models.CharField(max_length=50, choices=ALERT_TYPES)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    severity = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    date_issued = models.DateTimeField()

    def __str__(self):
        return f'{self.type} Alert - {self.location.name}'

class Alert(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
from django.db import models

class Alert(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    timestamp = models.DateTimeField()
    type = models.CharField(max_length=50, choices=[('important', 'Important'), ('normal', 'Normal')])

    def __str__(self):
        return self.title
