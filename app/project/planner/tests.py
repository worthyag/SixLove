from django.test import TestCase,  RequestFactory
from django.urls import reverse

from registration.models import CustomUser

from . import views

# Create your tests here.


class CalendarViewTest(TestCase):
    """Testing the calendar view works as expected."""

    def setUp(self) -> None:
        """"""
        self.factory = RequestFactory()
        self.user = CustomUser.objects.create(
            username="testuser",
            password="testpassword"
        )

    def helper_get_response_calendar_view(self):
        """
        A helper function that produces a response for the calendar view
        and logs the user in. (To reduce code repetition).
        """
        # Creating an instance of a GET request.
        request = self.factory.get(reverse("planner:calendar"))

        # Simulating a logged-in user manually.
        request.user = self.user

        # Testing the view.
        response = views.calendar(request)

        return response

    def test_calendar_view_loads(self):
        """"""
        # Sending a GET response to the calendar view.
        response = self.helper_get_response_calendar_view()

        # Checking whether the calendar view loads successfully.
        self.assertEqual(response.status_code, 200)
