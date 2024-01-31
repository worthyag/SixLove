import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import TennisSession

# Create your tests here.


def create_tennis_session(days: int = 0):
    """
    Creates a tennis session to reduce code redundancy / repetition 
    when running tests.
    """
    time = timezone.now() + datetime.timedelta(days=days)
    tennis_session = TennisSession(date=time)
    return tennis_session


def create_tennis_session_with_date_str(days: int = 0):
    """
    Creates a tennis session using a string rather than the datetime object to reduce
    repetition when running tests.
    """
    date = timezone.now() + datetime.timedelta(days=days)
    month = date.month if date.month > 10 else f"0{date.month}"
    day = date.day if date.day > 10 else f"0{date.day}"

    date_str = f"{date.year}-{month}-{day}"

    # For testing.
    print(f"Date: {date_str}")

    tennis_session = TennisSession(date=date_str)
    return tennis_session


class TennisSessionModelTests(TestCase):
    """Testing my is_tennis_session_scheduled_today() method."""

    def test_tennis_session_scheduled_today(self):
        """
        is_tennis_session_scheduled_today() returns True if a tennis session
        is scheduled today.
        """
        today_tennis_session = create_tennis_session()

        self.assertIs(
            today_tennis_session.is_tennis_session_scheduled_today(), True)

    def test_no_tennis_session_scheduled_today(self):
        """
        is_tennis_session_scheduled_today() returns False when no tennis session
        is scheduled today.
        """
        future_tennis_session = create_tennis_session(days=3)

        self.assertIs(
            future_tennis_session.is_tennis_session_scheduled_today(), False)

    def test_date_in_string_format_tennis_session_scheduled_today(self):
        """
        Tests whether is_tennis_session_scheduled_today() returns True if a tennis session
        is scheduled today and the date is given in a string format.
        """
        today_tennis_session = create_tennis_session_with_date_str()

        self.assertIs(
            today_tennis_session.is_tennis_session_scheduled_today(), True
        )

    def test_date_in_string_format_no_tennis_session_scheduled_today(self):
        """
        Tests whether is_tennis_session_scheduled_today() returns False if when no tennis session
        is scheduled today and the date is given in a string format.
        """
        future_tennis_session = create_tennis_session_with_date_str(days=3)

        self.assertIs(
            future_tennis_session.is_tennis_session_scheduled_today(), False
        )


class TennisSessionDeleteViewTests(TestCase):
    """Testing the delete view."""

    def setUp(self):
        """Creating a tennis session to test."""
        self.tennis_session = create_tennis_session(days=1)
        self.tennis_session.save()

    def test_delete_view_redirects_after_deletion(self):
        """
        Tests whether the user is redirected to the tennis session list after
        deleting a session.
        """
        # Getting the url for the delete view.
        url = reverse("delete-tennis-session", args=[self.tennis_session.id])

        # Deleting the session via a POST request.
        response = self.client.post(url)

        # Checking whether the response redirects to the view tennis sessions view.
        self.assertRedirects(response, reverse("tennis-sessions"))

    def test_tennis_sessions_deleted_from_database(self):
        """
        Tests whether tennis sessions are removed from the database when
        deleted.
        """
        # Getting the initial count.
        initial_count = TennisSession.objects.count()

        # Getting the url for the delete view.
        url = reverse("delete-tennis-session", args=[self.tennis_session.id])

        # Deleting the session via a POST request.
        self.client.post(url)

        # Checking whether the object count decreased by 1.
        self.assertEqual(TennisSession.objects.count(), initial_count-1)

    def test_delete_view_displays_confirmation(self):
        """
        Tests the delete view displays the confirmation message.
        """
        # Getting the url for the delete view.
        url = reverse("delete-tennis-session", args=[self.tennis_session.id])

        # Sending a GET response to the delete view.
        response = self.client.get(url)

        # Checking whether the delete view displays the message.
        self.assertContains(
            response,
            f'Are you sure you want to delete the session "{
                self.tennis_session.title}"?'
        )
