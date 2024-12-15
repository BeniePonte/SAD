from django.utils import timezone
from .models import DisasterAlert, Location
from django.contrib.auth.models import User
from django.test import TestCase

class DisasterAlertTestCase(TestCase):

    def setUp(self):
        # Créer un utilisateur de test
        self.user = User.objects.create_user(username='testuser', password='password')

        # Créer une localisation de test
        self.location = Location.objects.create(
            name='Test Location',
            latitude=12.34,
            longitude=56.78
        )

        # Créer un DisasterAlert avec timezone.now() pour date_issued
        self.alert = DisasterAlert.objects.create(
            user=self.user,
            type='earthquake',
            description="Test Earthquake Description",
            location=self.location,
            severity="High",
            date_issued=timezone.now()  # Utilisation de timezone.now() ici
        )

    def test_alert_content(self):
        # Vérifiez si l'alerte a été correctement créée
        self.assertEqual(self.alert.type, 'earthquake')
        self.assertEqual(self.alert.location.name, 'Test Location')
        self.assertEqual(self.alert.severity, 'High')
