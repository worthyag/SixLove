import datetime

from django.test import TestCase
from django.utils import timezone

from .models import TennisSession

# Create your tests here.


def create_tennis_session(date):
    """
    Creates a tennis session to reduce code redundancy / repetition 
    when running tests.
    """
    tennis_session = TennisSession(date=date)


class TennisSessionModelTests(TestCase):
    """Testing my is_tennis_session_scheduled_today() method."""

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

    def test_date_in_string_format_tennis_session_scheduled_today(self):
        """
        Tests whether is_tennis_session_scheduled_today() returns True if a tennis session
        is scheduled today and the date is given in a string format.
        """
        date = timezone.now()
        month = date.month if date.month > 10 else f"0{date.month}"
        day = date.day if date.day > 10 else f"0{date.day}"

        date_str = f"{date.year}-{month}-{day}"
        today_tennis_session = TennisSession(date=date_str)

        # For testing.
        print(f"Date: {date_str}")

        self.assertIs(
            today_tennis_session.is_tennis_session_scheduled_today(), True
        )

    def test_date_in_string_format_no_tennis_session_scheduled_today(self):
        """
        Tests whether is_tennis_session_scheduled_today() returns False if when no tennis session
        is scheduled today and the date is given in a string format.
        """
        date = timezone.now() + datetime.timedelta(days=3)
        month = date.month if date.month > 10 else f"0{date.month}"
        day = date.day if date.day > 10 else f"0{date.day}"

        date_str = f"{date.year}-{month}-{day}"
        future_tennis_session = TennisSession(date=date_str)

        # For testing.
        print(f"Date: {date_str}")

        self.assertIs(
            future_tennis_session.is_tennis_session_scheduled_today(), False
        )


class TennisSessionDeleteViewTests(TestCase):
    """Testing the delete view."""

    def test_tennis_sessions_removed_from_db_when_deleted(self):
        """
        Tests whether tennis sessions are removed from the database when
        deleted.
        """
