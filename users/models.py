from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    LOCATION_CHOICES = [
        ('girne', 'Girne'),
        ('lefkoşa', 'Lefkoşa'),
        ('lefke', 'Lefke'),
        ('iskele', 'İskele'),
        ('gazimağusa', 'Gazimağusa'),
        ('güzelyurt', 'Güzelyurt'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True)
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

class Location(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

class DisasterAlert(models.Model):
    ALERT_TYPES = [
        ('earthquake', 'Earthquake'),
        ('flood', 'Flood'),
        ('fire', 'Fire'),
        ('tsunami', 'Tsunami'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='users_disaster_alerts')  # Nom unique pour éviter les conflits
    type = models.CharField(max_length=50, choices=ALERT_TYPES)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    severity = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    date_issued = models.DateTimeField()

    def __str__(self):
        return f'{self.type} Alert - {self.location.name}'

class Alert(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
