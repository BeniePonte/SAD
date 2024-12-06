from django.contrib import admin
from .models import DisasterAlert, Location

@admin.register(DisasterAlert)
class DisasterAlertAdmin(admin.ModelAdmin):
    list_display = ['type', 'location', 'severity', 'date_created', 'date_issued']
    list_filter = ['type', 'severity', 'date_created']
    search_fields = ['type', 'location__name', 'description']

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['name', 'latitude', 'longitude']
    search_fields = ['name']
