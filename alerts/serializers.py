# alerts/serializers.py
from rest_framework import serializers
from .models import DisasterAlert

class DisasterAlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisasterAlert
        fields = '__all__'  # Adjust this to include the fields you want to serialize
