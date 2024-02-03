import datetime

from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.utils import timezone

from registration.models import CustomUser
from .models import TennisSession
from . import views

# Create your tests here.


class TennisViewsTest(TestCase):
    """Testing the tennis view work as expected."""

    def setUp(self) -> None:
        """"""
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = CustomUser.objects.create(
            username="testuser",
            password="testpassword"
        )

    def helper_get_response_tennis_view(self):
        """
        A helper function that produces a response for the tennis view.
        (To reduce code repetition).
        """
        # Creating an instance of a GET request.
        request = self.factory.get(reverse("tennis:tennis"))

        # Simulating a logged-in user manually.
        request.user = self.user

        # Testing the view.
        response = views.tennis(request)

        return response

    def test_tennis_view_with_no_tennis_sessions(self):
        """"""
        # Generating the response.
        response = self.helper_get_response_tennis_view()

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            "No tennis sessions scheduled for today."
        )

    def test_tennis_view_with_tennis_sessions(self):
        """"""
        # Getting today's day.
        today = timezone.now().date()

        # Adding a tennis session.
        TennisSession.objects.create(
            user=self.user,
            title="This is not a drill",
            notes="I repeat, this is not a drill",
            date=today,
        )

        # Generating the response.
        response = self.helper_get_response_tennis_view()

        self.assertEqual(response.status_code, 200)
        self.assertNotContains(
            response,
            "No tennis sessions scheduled for today."
        )


class AddViewTest(TestCase):
    """Testing the add view work as expected."""

    def setUp(self) -> None:
        """"""
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = CustomUser.objects.create(
            username="testuser",
            password="testpassword"
        )

    def helper_get_response_add_view(self):
        """
        A helper function that produces a response for the add view.
        """
        # Creating an instance of a GET request.
        request = self.factory.get(reverse("tennis:add"))

        # Simulating a logged-in user manually.
        request.user = self.user

        # Testing the view.
        response = views.add(request)

        return response

    def test_add_view_loads(self):
        """"""
        # Generating the response.
        response = self.helper_get_response_add_view()

        self.assertEqual(response.status_code, 200)
