import datetime

from django.test import TestCase, RequestFactory
from django.urls import reverse
# from django.contrib.auth.models import Users
# from django.contrib.auth.views import login

from registration.models import CustomUser
from . import views

# Create your tests here.


class TennisViewsTest(TestCase):
    """Testing the tennis views work as expected."""

    def setUp(self) -> None:
        """"""
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = CustomUser.objects.create(
            username="testuser",
            password="testpassword"
        )

    def test_tennis_view_with_no_tennis_sessions(self):
        """"""
        # Creating an instance of a GET request.
        request = self.factory.get(reverse("tennis:tennis"))

        # Simulating a logged-in user manually.
        request.user = self.user

        # Testing the view.
        response = views.tennis(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            "No tennis sessions scheduled for today."
        )
