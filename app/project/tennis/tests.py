import datetime

from django.test import TestCase
from django.urls import reverse
# from django.contrib.auth.models import Users
from registration.models import CustomUser

# Create your tests here.


class TennisViewsTest(TestCase):
    """Testing the tennis views work as expected."""

    def setUp(self) -> None:
        """"""
        self.user = CustomUser.objects.create(
            username="testuser",
            password="testpassword"
        )

    def test_tennis_view_with_no_tennis_sessions(self):
        """"""
        self.client.login(username=self.user.username,
                          password=self.user.password)

        response = self.client.get(reverse("tennis:tennis"))
        self.assertEqual(response.status_code, 302)
        self.assertContains(response, "No tennis sessions scheduled for today.")



