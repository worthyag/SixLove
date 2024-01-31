import datetime

from django.test import TestCase
from django.utils import timezone

from .models import TennisSession

# Create your tests here.


class TennisSessionModelTests(TestCase):
    # Testing my is_tennis_session_scheduled_today() method.
    def test_tennis_session_scheduled_today(self):
        """
        is_tennis_session_scheduled_today() returns True if a tennis session
        is scheduled today.
        """
        date = timezone.now()
        today_tennis_session = TennisSession(date=date)

        self.assertIs(
            today_tennis_session.is_tennis_session_scheduled_today(), True)

    def test_no_tennis_session_scheduled_today(self):
        """
        is_tennis_session_scheduled_today() returns False when no tennis session
        is scheduled today.
        """
        date = timezone.now() + datetime.timedelta(days=3)
        future_tennis_session = TennisSession(date=date)

        self.assertIs(
            future_tennis_session.is_tennis_session_scheduled_today(), False)
