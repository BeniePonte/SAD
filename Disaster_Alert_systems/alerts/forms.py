# alerts/forms.py
from django import forms
from .models import DisasterAlert

class DisasterAlertForm(forms.ModelForm):
    class Meta:
        model = DisasterAlert
        fields = ['type', 'location', 'description', 'severity', 'date_issued']