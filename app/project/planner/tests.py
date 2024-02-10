from django.test import TestCase,  RequestFactory
from django.urls import reverse

from registration.models import CustomUser
from tennis.models import TennisSession

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

    def test_calendar_view_url_accessible_by_name(self):
        # Ensure the view is accessible using its name
        self.client.login(
            username=self.user.username,
            password=self.user.password
        )

        response = self.client.get(reverse("planner:calendar"))

        # 302 since when using self.client it is redirecting.
        self.assertEqual(response.status_code, 302)

    # def test_calendar_view_uses_template(self):
    #     """"""
    #     self.client.login(
    #         username=self.user.username,
    #         password=self.user.password
    #     )

    #     response = self.client.get(reverse('planner:calendar'))

    #     # Checking whether the chosen view uses the template.
    #     self.assertTemplateUsed(
    #         response,
    #         "./planner/calendar.html"
    #     )

    def test_calendar_edit_tennis_session(self):
        """"""
        # Testing editing a TennisSession
        session = TennisSession.objects.create(
            user=self.user,
            title="Test Session",
            notes="Test Notes",
            date="2024-02-01",
            is_completed=False
        )

        # Creating an instance of a POST request.
        request = self.factory.post(reverse("planner:calendar"),
                                    {
            "session-id": session.id,
            "title": "Updated Session",
            "notes": session.notes,
            "date": session.date,
            "is_completed": session.is_completed
        })

        # Simulating a logged-in user manually.
        request.user = self.user

        # Testing the view.
        response = views.calendar(request)

        # Expecting a redirect.
        self.assertEqual(response.status_code, 302)

        # Checking if the TennisSession was updated
        updated_session = TennisSession.objects.get(id=session.id)

        self.assertEqual(updated_session.title, "Updated Session")

    def test_calendar_add_session(self):
        """"""
        # Creating an instance of a POST request.
        request = self.factory.post(reverse("planner:calendar"),
                                    {
            "session-id": "X",
            "title": "New Session",
            "notes": "New Notes",
            "date": "2024-03-01",
            "is_completed": "False"
        })

        # Simulating a logged-in user manually.
        request.user = self.user

        # Testing the view.
        response = views.calendar(request)

        # Expecting a redirect.
        self.assertEqual(response.status_code, 302)

        # Checking if the new TennisSession was added.
        new_session = TennisSession.objects.get(title="New Session")

        self.assertEqual(new_session.user, self.user)
        self.assertEqual(new_session.notes, "New Notes")
