import datetime

from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.utils import timezone

from registration.models import CustomUser
from .models import TennisSession
from . import views

# Create your tests here.


def generate_the_current_date():
    """
    Gets and returns today's day.
    """
    return timezone.now().date()


class TennisViewsTest(TestCase):
    """Testing the tennis view works as expected."""

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
        A helper function that produces a response for the tennis view
        and logs the user in. (To reduce code repetition).
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
        # Generating the response / logging in.
        response = self.helper_get_response_tennis_view()

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            "No tennis sessions scheduled for today."
        )

    def test_tennis_view_with_tennis_sessions(self):
        """"""
        # Adding a tennis session.
        TennisSession.objects.create(
            user=self.user,
            title="This is not a drill",
            notes="I repeat, this is not a drill",
            date=generate_the_current_date(),
        )

        # Generating the response / logging in.
        response = self.helper_get_response_tennis_view()

        self.assertEqual(response.status_code, 200)
        self.assertNotContains(
            response,
            "No tennis sessions scheduled for today."
        )


class AddViewTest(TestCase):
    """Testing the add view works as expected."""

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
        A helper function that produces a response for the add view
        and logs the user in.
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
        # Generating the response / logging in.
        response = self.helper_get_response_add_view()

        self.assertEqual(response.status_code, 200)

    def test_add_view_post_valid_form(self):
        """"""
        # Generating the response / logging in.
        response = self.helper_get_response_add_view()

        # Adding tennis sessions using the form.
        data = {
            "title": "This is not a drill",
            "notes": "I repeat, this is not a drill",
            "date": generate_the_current_date(),
        }

        # Submitting the form data.
        response = self.client.post(reverse('tennis:add'), data)

        # Testing that the page redirects upon successful form submission.
        self.assertEqual(response.status_code, 302)


class EditTennisSessionViewTest(TestCase):
    """Testing the edit tennis session view works as expected."""

    def setUp(self) -> None:
        """"""
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

        self.user = CustomUser.objects.create(
            username="testuser",
            password="testpassword"
        )

        # Adding a tennis session.
        self.tennis_session = TennisSession.objects.create(
            user=self.user,
            title="This will be edited",
            notes="I will add to this later.",
            date=generate_the_current_date(),
        )

    def helper_get_response_edit_tennis_session_view(self):
        """
        A helper function that produces a response for the edit tennis
        session view and logs the user in.
        """
        # Getting the edit page.
        request = self.factory.get(
            reverse("tennis:edit", args=[self.tennis_session.id])
        )

        # Simulating a logged-in user manually.
        request.user = self.user

        # Testing the view.
        response = views.edit_tennis_session(request, self.tennis_session.id)

        return response

    def test_edit_tennis_session_view_loads(self):
        """"""
        # Generating the response / logging in.
        response = self.helper_get_response_edit_tennis_session_view()

        self.assertEqual(response.status_code, 200)

    def test_edit_tennis_session_view_post_valid_form(self):
        """"""
        # Generating the response / logging in.
        response = self.helper_get_response_edit_tennis_session_view()

        # Editing tennis sessions using the form.
        data = {
            "title": "Updated session",
            "notes": "I told you that I would update my notes.",
            "date": generate_the_current_date(),
        }

        # Submitting the form data.
        response = self.client.post(reverse('tennis:edit',
                                            args=[self.tennis_session.id]),
                                    data)

        # Testing that the page redirects upon successful form submission.
        self.assertEqual(response.status_code, 302)
