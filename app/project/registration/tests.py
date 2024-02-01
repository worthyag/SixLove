from django.test import TestCase
from django.urls import reverse

# Create your tests here.


class RegistrationViewsTests(TestCase):
    """
    Testing the registration views work as expected.
    """

    def registration_view_uses_template(self, url_name: str, template: str):
        """
        Helper function to minimise code repetition.

        Parameters
        ----------
        """
        # Getting the url for the chosen view
        url = reverse(url_name)

        # Sending a GET response to the chosen view.
        response = self.client.get(url)

        # Checking whether the chosen view uses the template.
        self.assertTemplateUsed(
            response,
            f"./registration/{template}.html"
        )

    def test_home_view_uses_template(self):
        """
        Testing the the home view uses the given template.
        """
        # Getting the url for the home view
        url = reverse("home")

        # Sending a GET response to the home view.
        response = self.client.get(url)

        # Checking whether the home view uses the template.
        self.assertTemplateUsed(
            response,
            "./registration/index.html"
        )
