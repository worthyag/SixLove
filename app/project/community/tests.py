from django.test import TestCase, RequestFactory
from django.urls import reverse

from registration.models import CustomUser

from . import views

# Create your tests here.


class CommunityViewsTest(TestCase):
    """Testing the community views."""

    def setUp(self) -> None:
        """"""
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = CustomUser.objects.create(
            username="testuser",
            password="testpassword"
        )

    def helper_get_response_community_views(self, view):
        """
        A helper function that produces a response for the community view
        and logs the user in. (To reduce code repetition).
        """
        # Creating an instance of a GET request.
        request = self.factory.get(reverse(f"community:{view}"))

        # Simulating a logged-in user manually.
        request.user = self.user

        if view == "connect":
            # Testing the view.
            response = views.connect(request)
        elif view == "feed":
            # Testing the view.
            response = views.feed(request)
        elif view == "profile":
            # Testing the view.
            response = views.profile(request)
        elif view == "user":
            # Testing the view.
            response = views.user(request)
        elif view == "profile_settings":
            # Testing the view.
            response = views.profile_settings(request)

        return response

    def test_connect_view_loads(self):
        """"""
        # Generating the response / logging in.
        response = self.helper_get_response_community_views("connect")

        self.assertEqual(response.status_code, 200)

    def test_feed_view_loads(self):
        """"""
        # Generating the response / logging in.
        response = self.helper_get_response_community_views("feed")

        self.assertEqual(response.status_code, 200)

    def test_profile_view_loads(self):
        """"""
        # Generating the response / logging in.
        response = self.helper_get_response_community_views("profile")

        self.assertEqual(response.status_code, 200)

    def test_user_view_loads(self):
        """"""
        # Generating the response / logging in.
        response = self.helper_get_response_community_views("user")

        self.assertEqual(response.status_code, 200)

    def test_profile_settings_view_loads(self):
        """"""
        # Generating the response / logging in.
        response = self.helper_get_response_community_views("profile_settings")

        self.assertEqual(response.status_code, 200)
