from django.contrib import admin
from .models import DisasterAlert, Location

class DisasterAlertAdmin(admin.ModelAdmin):
    list_display = ('type', 'severity', 'location', 'date_created', 'date_issued')
    list_filter = ('severity', 'type')
    search_fields = ('description', 'type', 'location__name')

admin.site.register(DisasterAlert, DisasterAlertAdmin)
admin.site.register(Location)
